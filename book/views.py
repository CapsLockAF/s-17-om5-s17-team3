from django.shortcuts import render, redirect
from .models import *
from order.models import Order
from .create_bd import set_bd
from book.forms import BookForm
from django.core.paginator import Paginator
from rest_framework import viewsets
from .serializers import BookSerializer

num_items = 10


class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


def show_all_books(request):
    all_books = Book.get_all()
    paginator = Paginator(all_books, num_items)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    page_nums = range(page_obj.paginator.num_pages)
    return render(request, 'book/index.html',
                  {
                      'title': 'Books Information',
                      "heading": "All Books",
                      'page_obj': page_obj,
                      'page_nums': page_nums,
                      'state_sort': 'asc'
                  })


def show_book_by_id(request, book_id=0):
    book_by_id = Book.get_by_id(book_id)
    return render(request, 'book/book_by_id.html',
                  {
                      'title': "Book by id",
                      "heading": "Book by id",
                      "book_by_id": book_by_id,
                  })


def show_book_by_field(request, field_prop="id", field_value=""):
    def option(fp):
        if fp == "id":
            return Book.objects.filter(id=int(field_value))
        elif fp == "name":
            return Book.objects.filter(name=field_value)
        elif fp == "authors":
            a = Author.objects.get(name=field_value)
            return Book.objects.filter(authors=a.id)
        else:
            return []

    all_books = option(field_prop)
    paginator = Paginator(all_books, num_items)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    page_nums = range(page_obj.paginator.num_pages)
    return render(request, 'book/index.html',
                  {
                      'title': f"Books by {field_prop}:  {field_value}",
                      "heading": f"Books by {field_prop}: {field_value}",
                      'page_obj': page_obj,
                      'page_nums': page_nums,
                  })


def show_book_by_author(request, author_id=0):
    author_by_id = Author.get_by_id(author_id)
    author_books = Book.objects.filter(authors=author_id)
    titles = f"Books by author {author_by_id.name} {author_by_id.surname}" if author_books else "No Books by author"
    return render(request, 'book/books_by_author.html',
                  {
                      'title': titles,
                      "heading": titles,
                      "author_books": author_books,
                  })


def book_order(request, field_name="name", state_sort='asc'):
    books_order = Book.objects.all().order_by(f'{"-" if state_sort == "desc" else ""}{field_name}')
    paginator = Paginator(books_order, num_items)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    page_nums = range(page_obj.paginator.num_pages)
    return render(request, 'book/index.html',
                  {
                      'title': f'Sorted by {field_name}',
                      'page_obj': page_obj,
                      'page_nums': page_nums,
                  })


def show_ordered_books(request):
    ordered_books = list(Order.objects.select_related('book'))
    return render(request, 'book/index.html',
                  {
                      'title': f'Ordered Books',
                      'books': ordered_books,
                  })


def start(request):
    # for i in range(40, 1000, 10):
    set_bd(60)
    return render(request, 'book/index.html')


def book_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = BookForm()
        else:
            books = Book.objects.get(pk=id)
            form = BookForm(instance=books)
        return render(request, "book/book_form.html", {"form": form})
    else:
        if id == 0:
            form = BookForm(request.POST)
        else:
            books = Book.objects.get(pk=id)
            form = BookForm(request.POST, instance=books)
        if form.is_valid():
            form.save()
        return redirect('index')


def deleted_form(request, id):
    Book.delete_by_id(id)
    return redirect("index")
