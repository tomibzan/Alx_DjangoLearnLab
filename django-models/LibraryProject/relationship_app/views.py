from django.views.generic.detail import DetailView
from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Library

# Function-based view to list all books


def list_books(request):
    books = Book.objects.select_related(
        'author').all()  # Efficient query with author
    return render(request, 'list_books.html', {'books': books})


# Class-based view to show library details


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'

    # Optional: override get_context_data if needed
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()
        return context
