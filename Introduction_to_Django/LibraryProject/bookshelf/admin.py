from django.contrib import admin
from .models import Book

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_fiter = ("title", "author", "publication_year")


admin.site.register(Book)
