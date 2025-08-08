from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime

class Author(models.Model):
    """
    Represents an author of books.
    Each author can write multiple books (one-to-many relationship).
    """
    name = models.CharField(
        max_length=200,
        help_text="Enter the full name of the author."
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Book(models.Model):
    """
    Represents a book written by an author.
    Linked to Author via a ForeignKey (one-to-many).
    Includes title, publication year, and author.
    """
    title = models.CharField(
        max_length=200,
        help_text="Title of the book."
    )
    publication_year = models.IntegerField(
        validators=[
            MinValueValidator(1000, message="Year must be at least 1000."),
            MaxValueValidator(datetime.now().year, message="Publication year cannot be in the future.")
        ],
        help_text="Year the book was published."
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books',  # Allows accessing books via author.books.all()
        help_text="The author of this book."
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"

    class Meta:
        ordering = ['title']
# Create your models here.
