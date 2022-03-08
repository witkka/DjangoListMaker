"""
Views configuration for the input_manipulation application.
"""
from django.shortcuts import render, redirect
from .forms import TextInputForm
from .text_cleaning import get_word_list


def new(request):
    """Method for rendering new.html which contains the TextInputForm().
    Combines the 'new.html' template with initial context of form from the TextInputForm() method.
    When user fills in the form and submits data, receives request object and creates context comprising  of
    the word list containing unique words. This list populates the TextInputForm().
    Each word can be selected (form with checkboxes).
    If words are selected, method redirects to the 'list' view.

     Parameters
     ---------
     request: request object

     Returns
     -------
     HttpResponse object
    """
    if request.method == "POST":
        form = TextInputForm(request.POST)
        if form.is_valid():
            cleaned_form = form.cleaned_data
            text = cleaned_form.get("text")
            word_list = get_word_list(text)
            if "listSubmit" in request.POST:
                words = request.POST.getlist("choices")
                request.session["words"] = words
                return redirect("list")
            return render(
                request,
                "input_manipulation/new.html",
                context={"form": form, "word_list": word_list},
            )
    else:
        form = TextInputForm()
    return render(request, "input_manipulation/new.html", {"form": form})
