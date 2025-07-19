from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import (
    admin_view,
    librarian_view,
    member_view,
    register_view,
    list_books,
    LibraryDetailView
)

urlpatterns = [
    # Dashboard Views
    # Changed name for consistency
    path('admin-dashboard/', admin_view, name='admin_dashboard'),
    path('librarian-dashboard/', librarian_view, name='librarian_dashboard'),
    path('member-dashboard/', member_view, name='member_dashboard'),

    # Auth Views
    path('register/', register_view, name='register'),
    path(
        'login/',
        LoginView.as_view(
            template_name='relationship_app/login.html',
            redirect_authenticated_user=True  # Prevent logged-in users from accessing login
        ),
        name='login'
    ),
    path(
        'logout/',
        LogoutView.as_view(
            template_name='relationship_app/logout.html',
            next_page='home'  # Explicit redirect after logout
        ),
        name='logout'
    ),

    # Core Views
    path('', list_books, name='home'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
