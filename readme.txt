=========================================================================
DjangoListMaker, version '1.0.0', March, 2022.
This is README.txt,  user guide.
Author: Katarzyna Witkowska, https://github.com/witkka
=========================================================================

This package contains django project containing:
    - flashcards app containing main configuration and urls
    - text_manipulation app containing scripts responsible collecting text input,
    text manipulation: lowercasing, removing digits, punctuation and repeating words,
    List of words populates form values. User chooses which words should be further
    translated (checkboxes)
    - dictionary app responsible for making async. requests to dictionary api"
    'https://api.dictionaryapi.dev', as a result user can download a list of words,
    their translations, examples of sentences, synonyms and antonyms
    - scraper app responsible for scraping page 'https://www.lextutor.ca' which is a
    lexical corpus, as a result user is presented with a list of quotes containing
    chosen word
    - static_page app responsible for displaying static page
    - templates containing html files

-------------------------------------------------------------------------
To install the package:
> pip install -e .

To make migrations:
> py manage.py migrate

To run tests:
> pytest tests/

To start development server:
> manage.py runserver


