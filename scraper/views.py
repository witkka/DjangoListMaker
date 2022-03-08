"""
Configuration of the scraper app required for views.py.
"""
from django.shortcuts import render
from .forms import ContextForm
from .scraper import Quote


def context(request):
    """Method for rendering context.html which contains the ContextForm().
    Combines the 'context.html' template with initial context of form from the ContextForm() method.
    When user fills in the form using predefined dropdown menu, and submits data, receives request object and
    creates context comprising  of formatted string containing searched word and piece of text containing this word,
    from defined lexical database.
    If word could not be fined the lexical corpus, a message is displayed.

     Parameters
     ---------
     request: request object

     Returns
     -------
     HttpResponse object
    """
    form = ContextForm()
    if request.method == "POST":
        form = ContextForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            word = data.get("word")
            search_type = data.get("search_type")
            corpus_type = data.get("corpus_type")
            number_of_characters = data.get("number_of_characters")
            quote = Quote(search_type, word, corpus_type, number_of_characters)
            paragraph = quote.get_paragraph()
            if not paragraph:
                msg = (
                    f'We could not find your word. The word "{word}" is not in our database. '
                    f"Maybe try different corpus search"
                )
                return render(
                    request, "scraper/context.html", context={"form": form, "msg": msg}
                )
            else:
                lines = quote.get_clean_text(paragraph)
                msg = "This is all, we could find. Enjoy."
                return render(
                    request,
                    "scraper/context.html",
                    context={"form": form, "msg": msg, "lines": lines, "word": word},
                )
    return render(request, "scraper/context.html", context={"form": form})
