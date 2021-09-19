from django.shortcuts import render, redirect
from author.models import Author
from author.forms import AuthorForm
from django.core.paginator import Paginator

num_items = 5


def all_authors(request):
    authors=Author.get_all()
    paginator = Paginator(authors, num_items)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    page_nums = range(page_obj.paginator.num_pages)
    return render(request, "author/authors.html",
                  {
                      'title': 'Authors Information',
                      "heading": "All Authors",
                      'page_obj': page_obj,
                      'page_nums': page_nums
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
