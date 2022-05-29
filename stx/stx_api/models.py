from django.db import models


class Book(models.Model):
    book_external_id = models.IntegerField(null=True)
    title = models.CharField(max_length=400)
    authors = models.ManyToManyField('Author', related_name='books')
    publish_year = models.CharField(max_length=4)
    acquired = models.BooleanField()
    thumbnail = models.CharField(null=True, max_length=600)


class Author(models.Model):
    full_name = models.CharField(max_length=100)

