from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('book_name', 'author', 'publication_year', 'isbn', 'program')


# admin.site.register(Books)