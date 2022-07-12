from django.db import models
from django.utils.translation import gettext_lazy as _

class Author(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    description = models.TextField()


class Book(models.Model):

    class TypeBook(models.TextChoices):
        FANTASY = 'FA',_('Fantasy')
        HORROR = 'HO',_('Horror')
        COMEDY = 'CO',_('Comedy')
        THRILLER = 'TH',_('Thriller')

    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    realase_date = models.DateField()
    description = models.TextField()
    type = models.CharField(max_length=2,choices=TypeBook.choices)