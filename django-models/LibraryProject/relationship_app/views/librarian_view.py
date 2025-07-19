from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test


def is_librarian(user):
    return user.userprofile.role == 'Librarian'


@user_passes_test(is_librarian, login_url='/')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')
