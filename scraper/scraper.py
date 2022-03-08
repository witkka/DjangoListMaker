"""
Configuration for the scraper app, which enables scraping lexical corpus and processing obtained data.
"""
from bs4 import BeautifulSoup
import requests
import re


class Quote:
    """Class responsible for creating Quote object.

    Parameters
    ----------
    search_type: str
        Information if query should start with, end with, be equal to or contain given word.
    word: str
        Word that user is looking for.
    corpus: str
        Information about which lexical corpus the query should be performed on.
    characters: int
        Length of obtained data.

    Returns
    -------
    str: new url containing all required information to obtain data
    """

    def __init__(self, search_type, word, corpus, characters):
        self.characters = characters
        self.search_type = search_type
        self.word = word
        self.corpus = corpus
        self.start = "&".join(
            [
                "https://www.lextutor.ca/cgi-bin/conc/wwwassocwords.pl?lingo=English",
                "KeyWordFormat=",
                "Gaps=no_gaps",
                "store_dic=Eng_Eng",
                "is_refire=true",
                "Fam_or_Word=multi",
                "Source=https%3A%2F%2Fwww.lextutor.ca%2Fconc%2Feng%2F",
                "unframed=true",
            ]
        )
        self.end = "&".join(
            [
                "ColloSize=",
                "SortType=key",
                "AssocWord=",
                "AssocSide=either",
                "Maximum=15",
            ]
        )

    def get_search_type(self):
        """Method responsible for selecting search type."""
        return f"SearchType={self.search_type}"  # starts, ends, equals, contains

    def get_search_word(self):
        """Method responsible for selecting searched word."""
        return f"SearchStr={self.word}"

    def get_corpus(self):
        """Method responsible for selecting searched corpus type."""
        return f"Corpus={self.corpus}"  # acada_corp.txt, speech_10.txt, acada_corp.txt, BLaRC.txt

    def get_characters(self):
        """Method responsible for selecting length of text that chould be returned."""
        return f"LineWidth={self.characters}"

    def get_link(self):
        """Method responsible for combining into one link data required for sending request."""
        return (
            self.start
            + "&"
            + self.get_search_type()
            + "&"
            + self.get_search_word()
            + "&"
            + self.get_corpus()
            + "&"
            + self.end
            + "&"
            + self.get_characters()
        )

    def make_request(self):
        """Method responsible for making a request."""
        word_link = self.get_link()
        return requests.get(word_link)

    def make_soup(self):
        """Method responsible for creating beautiful soup object."""
        page = self.make_request()
        return BeautifulSoup(page.content, "html.parser")

    def get_text(self):
        """Method responsible for obtaining text from the soup object."""
        soup = self.make_soup()
        return soup.body.get_text()

    def get_paragraph(self):
        """Method responsible for selecting fragment of text (paragraph) containing required information"""
        text = self.get_text()
        pattern = (
            r"(?:Click any KEYWORD for more context\xa0\n)"
            r"([\s\S]*)(?:Distribution for " + f"{self.search_type} {self.word})"
        )
        return re.findall(pattern, text)

    @staticmethod
    def get_line(paragraph):
        """Method responsible for splitting text into lines."""
        return paragraph[0].split("\n\n\n")

    def get_clean_text(self, paragraph):
        """Method responsible for extracting data from selected paragraph."""
        clean = []
        for line in self.get_line(paragraph):
            l = re.sub(r"(\d\d\d\.)", "[...]", line)
            clean.append((l + line.strip() + "[...]"))
        return clean
