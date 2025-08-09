from django.shortcuts import render
from rest_framework import generics, filters
from django_filters import rest_framework as django_filters
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


class BookFilter(django_filters.FilterSet):
    """
    Custom filter class for Book model.
    Allows filtering by exact match or range.
    """
    title = django_filters.CharFilter(lookup_expr='icontains')
    author = django_filters.CharFilter(field_name='author__name', lookup_expr='icontains')
    publication_year = django_filters.NumberFilter()
    publication_year__gt = django_filters.NumberFilter(field_name='publication_year', lookup_expr='gt')
    publication_year__lt = django_filters.NumberFilter(field_name='publication_year', lookup_expr='lt')

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']


class BookListView(generics.ListAPIView):
    """
    Retrieve a list of all books with filtering, searching, and ordering.
    - Filtering: by title, author, publication_year (exact or range)
    - Search: in title and author name
    - Ordering: by title, publication_year, author name
    """
    queryset = Book.objects.select_related('author').all()
    serializer_class = BookSerializer
    filter_backends = [
        django_filters.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_class = BookFilter  # Use custom filter
    search_fields = ['title', 'author__name']  # Fields to search
    ordering_fields = ['title', 'publication_year', 'author__name']
    ordering = ['title']  # Default ordering

