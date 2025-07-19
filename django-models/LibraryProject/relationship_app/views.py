from django.views.generic.detail import DetailView
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Book, Library, UserProfile

# === Existing Views ===


@login_required
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')


# === New Role-Based Views with Access Control ===
def is_admin(user):
    try:
        return user.userprofile.role == 'Admin'
    except UserProfile.DoesNotExist:
        return False


def is_librarian(user):
    try:
        return user.userprofile.role == 'Librarian'
    except UserProfile.DoesNotExist:
        return False


def is_member(user):
    try:
        return user.userprofile.role == 'Member'
    except UserProfile.DoesNotExist:
        return False


@user_passes_test(is_admin, login_url='/')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')


@user_passes_test(is_librarian, login_url='/')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')


@user_passes_test(is_member, login_url='/')
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
