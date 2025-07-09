from django.contrib import admin
from .models import Book

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    List_fiter = ("title", "author", "publication_year")


admin.site.register(Book)
