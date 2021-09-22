from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField
from .models import Book
from author.models import Author


class AuthorSerializer(PrimaryKeyRelatedField, serializers.ModelSerializer):
    class Meta:
        model: Author


class BookSerializer(serializers.HyperlinkedModelSerializer):
    authors = AuthorSerializer(many=True, queryset=Author.objects.all())

    class Meta:
        model = Book
        fields = ('id', 'url', 'name', 'description', 'count', 'authors')
