from django.db import models


class Book(models.Model):
    external_id = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=400, blank=False)
    authors = models.ManyToManyField("Author", related_name="books", blank=False)
    published_year = models.CharField(max_length=4, blank=False)
    acquired = models.BooleanField(blank=False)
    thumbnail = models.CharField(null=True, max_length=600, blank=True)


class Author(models.Model):
    full_name = models.CharField(max_length=100, blank=False)

