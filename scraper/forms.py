"""
Configuration for the forms of the 'scraper' app.
Contains definition of choices for the dropdown menu of the form created by the class ContextForm,
used to collect data from a lexical corpus from page: https://www.lextutor.ca"""
from django import forms

SEARCH_TYPES = (
    ("starts", "starts with word"),
    ("ends", "ends with word"),
    ("equals", "equals to word"),
    ("contains", "contains word"),
)

CORPUS_CHOICES = (
    ("acada_corp.txt", "academic"),
    ("speech_10.txt", "spoken"),
    ("BLaRC.txt", "written"),
)

CHARACTER_NUMBER_CHOICES = (("50", "50"), ("100", "100"), ("300", "300"))


class ContextForm(forms.Form):
    """
    Creates a ContextForm class inheriting from forms.Form
    This form class has named fields: 'word', 'search_type', 'corpus_type', 'number_of_characters', which are mapped
    to HTML form <input> elements.
    Fields have predefined values and are displayed on page as a dropdown menu.
    """

    word = forms.CharField(max_length=20)
    search_type = forms.ChoiceField(choices=SEARCH_TYPES)
    corpus_type = forms.ChoiceField(choices=CORPUS_CHOICES)
    number_of_characters = forms.ChoiceField(choices=CHARACTER_NUMBER_CHOICES)
