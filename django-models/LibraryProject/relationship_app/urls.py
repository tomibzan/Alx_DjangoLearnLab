
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('register/', views.register_view, name='register'),
    
    # Use Django's built-in LoginView and LogoutView
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    
    path('', views.list_books, name='home'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]