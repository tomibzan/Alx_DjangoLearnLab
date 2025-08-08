from rest_framework import serializers
from .models import Author, Book
from datetime import datetime


class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.
    - Includes all fields: title, publication_year, author.
    - Adds custom validation to ensure publication_year is not in the future.
    """

    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        """
        Custom validation: Ensure publication year is not in the future.
        """
        if value > datetime.now().year:
            raise serializers.ValidationError(
                f"Publication year cannot be in the future. Got: {value}"
            )
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.
    - Includes the author's name.
    - Nested serialization of related books using BookSerializer.
    - 'books' is a reverse foreign key (via related_name='books').
    """
    books = BookSerializer(many=True, read_only=True)  # Nested serializer

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']