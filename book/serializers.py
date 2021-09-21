from rest_framework import serializers
from .models import Book
from author.serializers import AuthorSerializer


class BookSerializer(serializers.HyperlinkedModelSerializer):
    authors = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = ('id', 'url', 'name', 'description', 'count', 'authors')
