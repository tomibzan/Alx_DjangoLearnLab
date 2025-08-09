from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer


class BookListView(generics.ListAPIView):
    """
    Retrieve a list of all books.
    - Read-only access for everyone (authenticated or not).
    - Returns serialized list of books.
    """
    queryset = Book.objects.select_related('author').all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Read allowed for all


class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieve details of a single book by ID.
    - Public read access.
    """
    queryset = Book.objects.select_related('author').all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'pk'


class BookCreateView(generics.CreateAPIView):
    """
    Create a new book.
    - Only accessible to authenticated users.
    - Validates data via BookSerializer (e.g., publication_year not in future).
    """
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Optional: Add custom logic during creation.
        Example: Log who created the book (if needed later).
        """
        # You can add custom side effects here
        serializer.save()


class BookUpdateView(generics.UpdateAPIView):
    """
    Update an existing book.
    - Only accessible to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'


class BookDeleteView(generics.DestroyAPIView):
    """
    Delete a book by ID.
    - Only accessible to authenticated users.
    """
    queryset = Book.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        """
        Optional: Add logic before deletion (e.g., logging).
        """
        super().perform_destroy(instance)
# Create your views here.
