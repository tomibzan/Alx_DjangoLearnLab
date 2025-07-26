from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from django.db import models
from .models import Book, Article
from .forms import ExampleForm, ArticleForm, BookSearchForm


def bookshelf(request):
    return HttpResponse("Welcome to the Bookshelf!")

# Book views with proper security measures


def book_list(request):
    """Display list of books - no user input, minimal security risk"""
    books = Book.objects.all().order_by('title')  # Safe ORM usage
    return render(request, 'bookshelf/book_list.html', {'books': books})


def book_create(request):
    """Create a new book with proper CSRF and input validation"""
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Safe ORM usage - no direct SQL injection risk
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()

    return render(request, 'bookshelf/form_example.html', {'form': form})


def book_edit(request, pk):
    """Edit an existing book"""
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)

    return render(request, 'bookshelf/form_example.html', {'form': form})


def book_search(request):
    """Secure search functionality using Django forms and ORM"""
    form = BookSearchForm(request.GET)
    books = []

    if form.is_valid():
        query = form.cleaned_data['query']
        if query:
            # Safe parameterized query using Django ORM
            # This prevents SQL injection automatically
            books = Book.objects.filter(
                models.Q(title__icontains=query) |
                models.Q(author__icontains=query)
            )

    return render(request, 'bookshelf/book_search.html', {
        'form': form,
        'books': books
    })

# Article views with permission-based security


@permission_required('bookshelf.can_view', raise_exception=True)
def article_list(request):
    """Display articles with proper permission checking"""
    # Safe ORM usage - parameterized queries prevent SQL injection
    articles = Article.objects.filter(published=True).order_by('-id')
    return render(request, 'bookshelf/article_list.html', {'articles': articles})


@permission_required('bookshelf.can_create', raise_exception=True)
def article_create(request):
    """Create article with CSRF protection and input validation"""
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            # Safe ORM usage - no string concatenation or direct SQL
            form.save()
            return redirect('article_list')
    else:
        form = ArticleForm()

    return render(request, 'bookshelf/article_form.html', {'form': form})


@permission_required('bookshelf.can_edit', raise_exception=True)
def article_edit(request, pk):
    """Edit article with proper security measures"""
    # get_object_or_404 prevents information leakage through error messages
    article = get_object_or_404(Article, pk=pk)

    if request.method == 'POST':
        # CSRF protection handled automatically
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
        form = ArticleForm(instance=article)

    return render(request, 'bookshelf/article_form.html', {'form': form, 'article': article})


@permission_required('bookshelf.can_delete', raise_exception=True)
def article_delete(request, pk):
    """Delete article with CSRF protection"""
    # Safe object retrieval
    article = get_object_or_404(Article, pk=pk)

    if request.method == 'POST':
        # CSRF token validation handled by middleware
        article.delete()
        return redirect('article_list')

    return render(request, 'bookshelf/article_confirm_delete.html', {'article': article})
