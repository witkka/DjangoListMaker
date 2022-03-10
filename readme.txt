=========================================================================
DjangoListMaker, version '1.0.0', March, 2022.
This is README.txt,  user guide.
Author: Katarzyna Witkowska, https://github.com/witkka
Demo: https://desolate-badlands-81481.herokuapp.com/
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
set the environ. variable:
> pytest --ds=flashcards.settings

> pytest tests/

To start development server:
> manage.py runserver

-------------------------------------------------------------------------
User guide

./
Starter page containing links to all components of this app

./new
Page containing form for submitting text or word list.
After submitting, the same page displays a list of lowercased, cleaned and
unique words from the submitted text.
User checks checkboxes to select words, they want to translate

./list
Page containing word and its translations from 'https://api.dictionaryapi.dev'
User can download this list as a .txt document to their device.

./word_check
Page containing a form, when entered, a word is searched for in a dictionary.
The same page displays results.

./context
Page contains form, that allows the user to check a particular word in a
lexical corpus
