from django.urls import path
from . import views

urlpatterns = [
    path('bookshelf/', views.bookshelf, name='bookshelf'),
]
