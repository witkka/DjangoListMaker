"""
text_cleaning configuration
"""
import string
from collections import Counter


def clean_text(text=None):
    """Method for string manipulation
    Parameters
    ----------
    text: str
        string is manipulated to remove all digits and punctuation signs

    Returns
    -------
    str: lowercased if text input was not none
    None: if text input was None"""
    if text is not None:
        raw_text = str(text)
        rubbish = string.digits + string.punctuation + "—"
        translation = str.maketrans("", "", rubbish)
        return raw_text.lower().translate(translation)
    return None


def get_word_list(text):
    """
    Method creates a lit of unique words from string

    Parameters
    ----------
    text: str

    Returns
    -------
    list: if text was not None
    None: if text was None
    """
    if clean_text(text) is not None:
        flatten_list = [word for line in clean_text(text).split() for word in line.strip().split(" ") if word != '']
        clean_list = sorted(Counter(flatten_list).keys())
        if len(clean_list) > 0:
            return clean_list
    return None
