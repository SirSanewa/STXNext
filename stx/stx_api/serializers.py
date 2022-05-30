from rest_framework import serializers
from .models import Book, Author


class AuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ("full_name", )


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorsSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ("id", "external_id", "title", "authors", "published_year", "acquired", "thumbnail")
