# api/views.py

from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer


class BookList(generics.ListAPIView):
    """
    API endpoint that lists all books (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows full CRUD operations:
    - List all books
    - Retrieve a single book
    - Create, update, delete books
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
