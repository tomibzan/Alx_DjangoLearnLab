from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer


class BookList(ListAPIView):
    """
    API endpoint that lists all books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
# Create your views here.
