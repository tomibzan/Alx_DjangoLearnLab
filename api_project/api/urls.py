from django.urls import path
from . import views

app_name = "api"

urlpatterns = [
    path('books/', views.BookList.as_view(), name='book-list'),
]
