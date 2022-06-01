from rest_framework import serializers
from .models import Book, Author


class BookReadSerializer(serializers.ModelSerializer):
    authors = serializers.SerializerMethodField("get_author_fullnames")

    class Meta:
        model = Book
        fields = ("id", "external_id", "title", "authors", "acquired", "published_year", "thumbnail")

    def get_author_fullnames(self, obj):
        fullname_list = Author.objects.filter(book=obj).values_list("fullname", flat=True)
        return fullname_list


class BookWriteSerializer(serializers.ModelSerializer):
    authors = serializers.ListField()

    class Meta:
        model = Book
        fields = "__all__"

    def create(self, validated_data):
        authors = validated_data.pop("authors")
        new_book = Book.objects.create(**validated_data)

        for author_name in authors:
            new_author, _ = Author.objects.get_or_create(fullname=author_name)
            new_author.save()
            new_book.authors.add(new_author)

        return new_book

    def update(self, instance, validated_data):
        if validated_data.get("authors"):
            authors = validated_data.pop("authors")
            instance.authors.clear()

            for author_name in authors:
                new_author, _ = Author.objects.get_or_create(fullname=author_name)
                new_author.save()
                instance.authors.add(new_author)

        return super().update(instance, validated_data)
