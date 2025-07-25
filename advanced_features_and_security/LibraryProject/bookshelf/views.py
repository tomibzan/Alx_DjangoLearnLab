from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from .models import Article


def bookshelf(request):
    return HttpResponse("Welcome to the Bookshelf!")


@permission_required('bookshelf.can_view', raise_exception=True)
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'bookshelf/article_list.html', {'articles': articles})


@permission_required('bookshelf.can_create', raise_exception=True)
def article_create(request):
    if request.method == 'POST':
        # logic to save new article
        pass
    return render(request, 'bookshelf/article_form.html')


@permission_required('bookshelf.can_edit', raise_exception=True)
def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        # logic to update article
        pass
    return render(request, 'bookshelf/article_form.html', {'article': article})


@permission_required('bookshelf.can_delete', raise_exception=True)
def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('book_list')
    return render(request, 'bookshelf/article_confirm_delete.html', {'article': article})
