from django.shortcuts import render
from .forms import SearchForm
from django.http import HttpResponseRedirect

from . import util



def index(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data["form"]
            if query in util.list_entries():
                return HttpResponseRedirect(f"/wiki/{query}")
            elif any(query in i for i in util.list_entries()):
                entry_result = [entry for entry in util.list_entries() if query in entry]
                return render(request, "encyclopedia/index.html",{
        "entries": entry_result,
        "form": form
    })
   
    form = SearchForm()
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "form": form  
    })



   

def article(request, title):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data["form"]
            if query in util.list_entries():
                return HttpResponseRedirect(f"/wiki/{query}")
    else:
        form = SearchForm()

    content = util.get_entry(title)
    if content:
        return render(request, "encyclopedia/article.html",
                      {
                          "content": content,
                          "form": form
                      })
    else:
        return render(request, "encyclopedia/index.html")