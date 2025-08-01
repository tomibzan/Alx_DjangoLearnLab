from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

# Function-Based View: List all books


def list_books(request):
    """View to list all books with their authors."""
    books = Book.objects.select_related('author').all()  # Efficient query
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-Based View: Display Library Details


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add related books with their authors (efficient query)
        context['books'] = self.object.books.all().select_related('author')
        return context
