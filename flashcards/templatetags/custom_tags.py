"""
Custom_tags config for flashcards project. It enables registering custom tag filter

"""
from django import template
from django.utils import safestring
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name='highlight')
@stringfilter
def highlight_text(text, search):
    """ Method creates custom tag which adds <strong> tag to given part of text """
    highlighted = text.replace(search.upper(), '<strong>{}</strong>'.format(search.upper()))
    return safestring.mark_safe(highlighted)
