from django import forms
from .models import Book
from .models import Author


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ("name", "description", "count", "authors")
