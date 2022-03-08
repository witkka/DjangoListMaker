"""
Temps module provides helper functions for sending requests, obtaining, sorting and formatting data from json file
Forms module provides classes inheriting from forms.Form
"""
import requests
from django.shortcuts import render, redirect
from .temps import (
    get_entry_translation_tuple,
    get_translations,
    format_text,
    create_document,
)
from .forms import DictionaryForm, TranslationForm


async def word_list_page(request):
    """Method for showing a list of translations
    Parameters
    ---------
    request: request object
    """
    words = request.session.get("words")
    translations, invalid = await get_translations(words)

    text = await format_text(translations)

    request.session["text"] = text

    if request.method == "POST":
        form = TranslationForm(request.POST)
        if form.is_valid():
            return redirect(download_list(request))
    return render(
        request,
        "dictionary/list.html",
        context={"translations": translations, "invalid": invalid},
    )


def download_list(request):
    """Download a document based on translated words"""
    text = request.session.get("text")
    return create_document(text)


def check_word_form(request):
    """Single word check with extended definitions, synonyms, examples, antonyms and origin"""
    if request.method == "POST":
        form = DictionaryForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            word = cd.get("word")
            with requests.Session().get(
                f"https://api.dictionaryapi.dev/api/v2/entries/en_US/{word}"
            ) as res:
                if res.status_code == 200:
                    data = res.json()
                    translations = []
                    for n in range(len(data)):
                        translations.append(get_entry_translation_tuple(data, n))
                    return render(
                        request,
                        "dictionary/check.html",
                        context={"translations": translations, "form": form},
                    )
                else:
                    message = f'"{word}" was not found in the dictionary'
            return render(
                request,
                "dictionary/check.html",
                context={"form": form, "message": message},
            )
    else:
        form = DictionaryForm()
    return render(request, "dictionary/check.html", context={"form": form})
