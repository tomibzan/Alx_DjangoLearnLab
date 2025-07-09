from django.contrib import admin
from .models import Book

# Register your models here.
admin.site.register(Book)
admin.ModelAdmin.list_display = ('title', 'author', 'publication_year')
