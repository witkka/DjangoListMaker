"""
Module asyncio responsible for async. functions
"""
from .dictionary import Entry
import asyncio
import aiohttp
from collections import namedtuple
from tempfile import NamedTemporaryFile
import mimetypes
import os
from django.http import HttpResponse


def make_word_namedtuple(word, definitions):
    """
    Helper function for easy object excess in template
    Function creates namedtuple which can be accessed by name in the template.

    Parameters
    ----------
    word: str
    definitions: str

    Returns
    -------
    namedtuple
    """
    Translations = namedtuple("Translations", ["word", "definitions"])
    return Translations(word, definitions)


def get_entry_translation_tuple(data, n):
    """
    Helper function for easy object excess in template, that can be accessed by name.

    Parameters
    ----------
    data: json
    n: int
        Index number to access data

    Returns
    -------
    namedtuple
    """
    e = Entry(data, n)
    Translations = namedtuple(
        "Translations", ["word", "phonetic", "audio", "origin", "speech", "definitions"]
    )
    Definitions = namedtuple(
        "Definitions", ["definition", "example", "synonym", "antonym"]
    )

    return Translations(
        e.get_word(),
        e.get_phonetic(),
        e.get_audio(),
        e.get_origin(),
        e.get_parts_of_speech(),
        [
            Definitions(
                e.get_definition(n),
                e.get_example(n),
                e.get_synonyms(n),
                e.get_antonyms(n),
            )
            for n in range(len(e.get_definitions()))
        ],
    )


async def get_word_data(ses, word):
    """
    Helper function to collect single action async
    Function makes requests to the dictionary for a given word,
    if the code_status is 200, collects json data.

    Parameters
    ----------
    ses: session
    word: str

    Returns
    ------
    Two lists: invalid words, that were not found in the dictionary and translations found in the dictionary
    for given words.
    """
    invalid = []
    translations = []
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en_US/{word}"
    async with ses.get(url) as res:
        if res.status == 200:
            data = await res.json()
            e = Entry(data, 0)
            translations.append(
                make_word_namedtuple(
                    e.get_word(),
                    [
                        e.get_definition(n).strip(".")
                        for n in range(len(e.get_definitions()))
                    ],
                )
            )
        else:
            invalid.append(word)
    return invalid, translations


async def get_translations(words):
    """
    Asynchronous method to get data from json
    Function gets word list than loops ofer it to obtain awaitable object that represents a result of an asynchronous
    operation of the get_word_data method.

    Parameters
    ----------
    words: list

    Returns
    -------
    Two lists: "translations" containing data collected from the dictionary and "invalid" containing list of words that
    were not found in the dictionary
    """
    actions = []
    translations = []
    invalid = []

    async with aiohttp.ClientSession() as ses:
        for word in words:
            actions.append(asyncio.ensure_future(get_word_data(ses, word)))

        word_data = await asyncio.gather(*actions)
        for wd in word_data:
            if wd[1]:
                translations.append(wd[1])
            if wd[0]:
                invalid.append(wd[0])
    return translations, invalid


async def format_text(translations):
    """
    Method formats text to send to a tempfile

    Parameters
    ----------
    translations: list

    Returns
    -------
    str
    """
    temp = []
    for translation in translations:
        temp.append(f"{translation[0].word}: {', '.join(translation[0].definitions)}")
    return "\n\n".join(temp)


def create_document(text):
    """
    Method creates tempfile containing words and translations.
    Tempfile is accessible for download and cleaned up after current session.
    """
    with NamedTemporaryFile(suffix=".txt", mode="a+", encoding="utf-8") as f:
        f.write(text)
        f.seek(0)
        data = f.read()
        response = HttpResponse(data)
        response["content_type"] = mimetypes.guess_type(f.name)
        response["Content-Disposition"] = "attachment; filename=" + os.path.basename(
            "my_list.txt"
        )
        return response
