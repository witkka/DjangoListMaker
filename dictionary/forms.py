"""
Forms configuration. It enables creating form classes inheriting from forms.Form
"""
from django import forms


class DictionaryForm(forms.Form):
    """
    Creates a DictionaryForm class inheriting from forms.Form
    This form class has one field named 'word' which is mapped to HTML form <input> element
    """

    word = forms.CharField(max_length=20)


class TranslationForm(forms.Form):
    """
    Creates a DictionaryForm class inheriting from forms.Form
    This form class has one field named 'translation' which is mapped to HTML form <input> element
    """

    translation = forms.CharField(max_length=500, widget=forms.Textarea())
