from django import forms
from django.forms.models import ModelMultipleChoiceField
from .models import Book
from .models import Author


class AuthorsChoiceField(ModelMultipleChoiceField):

    def label_from_instance(self, obj):
        return f'{obj.name} {obj.surname} "{obj.patronymic}"'


class BookForm(forms.ModelForm):
    authors = AuthorsChoiceField(queryset=Author.objects.all())

    class Meta:
        model = Book
        fields = ("name", "description", "count", "authors")
