"""
Forms configuration. It enables creating form classes inheriting from forms.Form
"""
from django import forms


class TextInputForm(forms.Form):
    """
        Creates a TextInputForm class inheriting from forms.Form
        This form class has one field named 'text' which is mapped to HTML form <input> element
        """
    text = forms.CharField(
        max_length=500,
        widget=forms.Textarea())


