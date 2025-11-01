from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13, default='0000000000000')  # default added to avoid migration errors

    def __str__(self):
        return self.title
