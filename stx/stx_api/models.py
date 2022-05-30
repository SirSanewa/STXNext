from django.db import models


class Book(models.Model):
    external_id = models.IntegerField(null=True)
    title = models.CharField(max_length=400)
    authors = models.ManyToManyField("Author")
    published_year = models.IntegerField()
    acquired = models.BooleanField()
    thumbnail = models.CharField(null=True, max_length=600)

    class Meta:
        unique_together = ("title", "published_year",)


class Author(models.Model):
    fullname = models.CharField(max_length=100)
