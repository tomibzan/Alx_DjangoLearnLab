from django.urls import path
from . import views

app_name = 'relationship_app'  # Namespace

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(),
         name='library_detail'),
]
