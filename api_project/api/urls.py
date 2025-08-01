from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import BookList, BookViewSet  # Import both views

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

# Combine your URLs
urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),

    # Add all CRUD routes under /books_all/
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
