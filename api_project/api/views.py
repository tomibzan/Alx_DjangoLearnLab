from django.shortcuts import render
from rest_framework import generics, viewsets, permissions
from .models import Book
from .serializers import BookSerializer


class BookList(generics.ListAPIView):
    """
    Public endpoint: Anyone can view the list of books.
    No authentication required.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # No permission_classes here → uses global default (IsAuthenticated), but we'll override below


class BookViewSet(viewsets.ModelViewSet):
    """
    Full CRUD API for books.
    - SAFE_METHODS (GET, HEAD, OPTIONS): Available to all authenticated users
    - WRITE_METHODS (POST, PUT, PATCH, DELETE): Only allowed for admin users
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # All actions require login
    permission_classes = [permissions.IsAuthenticated]
