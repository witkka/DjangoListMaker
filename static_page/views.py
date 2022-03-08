"""
Configuration for the views.py of the static_page app.
"""
from django.shortcuts import render


def home(request):
    """Method responsible for rendering the home page from the home.html template.

    Parameters
    ---------
    request: request object

    Returns
    -------
    HttpResponse object
    """
    return render(request, "static_page/home.html")
