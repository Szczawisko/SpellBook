from django.contrib import admin

from .models import Author,Book

class BooksInline(admin.StackedInline):
    model = Book
    extra = 1

class AuthorAdmin(admin.ModelAdmin):
    inlines = [BooksInline]

admin.site.register(Author,AuthorAdmin)
admin.site.register(Book)
