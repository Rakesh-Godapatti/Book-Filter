from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    language = models.CharField(max_length=50)
    subjects = models.TextField()
    bookshelves = models.TextField()
    mime_types = models.TextField()
    downloads = models.IntegerField(default=0)

    def __str__(self):
        return self.title
