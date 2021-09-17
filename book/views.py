from django.shortcuts import render
from .models import *
from order.models import Order


def show_all_books(request):
    all_books = Book.get_all()
    return render(request, 'book/index.html',
                  {
                      'title': 'Books Information',
                      "heading": "All Books",
                      'books': all_books,
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
    return render(request, 'book/index.html',
                  {
                      'title': f"Books by {field_prop}:  {field_value}",
                      "heading": f"Books by {field_prop}: {field_value}",
                      "books": all_books,
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
    return render(request, 'book/index.html',
                  {
                      'title': f'Sorted by {field_name}',
                      'books': books_order,
                  })


def show_ordered_books(request):
    ordered_books = list(Order.objects.select_related('book'))
    print('ffffffffffffffffffffff', ordered_books)
    return render(request, 'book/index.html',
                  {
                      'title': f'Ordered Books',
                      'books': ordered_books,
                  })




def start(request):
    books_list = []
    for i in range(1, 100):
        book1 = Book.create(f'Book-{i}', f'Description{i}', i*2, [f'Author{i}', f'Author{i*10}'],)
        books_list.append(book1)
    return render(request, 'book/start.html')

