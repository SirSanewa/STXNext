from django.db import models


class Book(models.Model):
    external_id = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=400)
    authors = models.ManyToManyField("Author")
    published_year = models.IntegerField(null=True)
    acquired = models.BooleanField(default=False)
    thumbnail = models.CharField(null=True, max_length=600)

    class Meta:
        unique_together = ("title", "external_id",)


class Author(models.Model):
    fullname = models.CharField(max_length=100)
