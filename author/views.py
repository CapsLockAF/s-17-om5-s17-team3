from django.shortcuts import render, redirect
from .models import *
from author.models import Author
from author.forms import AuthorForm


def all_authors(request):
    authors=Author.get_all()
    return render(request, "author/authors.html",
                  {
                      'title': 'Authors Information',
                      "heading": "All Authors",
                      'authors': authors,
                  })


def author_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = AuthorForm()
        else:
            authors = Author.objects.get(pk=id)
            form = AuthorForm(instance=authors)
        return render(request, "author/authors_form.html", {"form":form})
    else:
        if id == 0:
            form = AuthorForm(request.POST)
        else:
            authors = Author.objects.get(pk=id)
            form = AuthorForm(request.POST, instance=authors)
        if form.is_valid():
            form.save()
        return redirect("/author")


def delete_author(request, id):
    Author.delete_by_id(id)
    return redirect("/author")
