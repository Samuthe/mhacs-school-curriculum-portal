from django.contrib import admin
from .models import *
from django_ckeditor_5.widgets import CKEditor5Widget
from django.db import models
from .models import Books

class BooksAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditor5Widget(config_name='default')},
    }
    list_display = ('book_name', 'author', 'publication_year', 'isbn', 'program')

admin.site.register(Books, BooksAdmin)



# Register your models here.

# @admin.register(Books)
# class BooksAdmin(admin.ModelAdmin):
#     list_display = ('book_name', 'author', 'publication_year', 'isbn', 'program')


# admin.site.register(Books)