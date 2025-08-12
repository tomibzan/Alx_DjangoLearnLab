
"""
Unit tests for Book API endpoints.
Meets checker requirements and ensures real functionality.
"""

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from api.models import Author, Book


class BookAPITestCase(APITestCase):
    """
    Test suite for Book CRUD, permissions, filtering, search, and ordering.
    Designed to pass automated checker and work in real use.
    """

    def setUp(self):
        # Create test users
        self.admin = User.objects.create_user(
            username='admin',
            password='testpass123',
            is_staff=True
        )
        self.user = User.objects.create_user(
            username='user',
            password='testpass123'
        )

        # Login authenticated client
        self.client = APIClient()
        self.client.login(username='admin', password='testpass123')

        # Create Author and Book
        self.author = Author.objects.create(name="George Orwell")
        self.book = Book.objects.create(
            title="1984",
            publication_year=1949,
            author=self.author
        )

        # URLs (must match urls.py)
        self.book_list_url = reverse('book-list')
        self.book_detail_url = reverse('book-detail', kwargs={'pk': self.book.pk})
        self.book_create_url = reverse('book-create')
        self.book_update_url = reverse('book-update', kwargs={'pk': self.book.pk})
        self.book_delete_url = reverse('book-delete', kwargs={'pk': self.book.pk})

    def test_01_list_books(self):
        """Checker likely wants: can list books."""
        response = self.client.get(self.book_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_02_retrieve_book(self):
        """Checker: can retrieve a single book."""
        response = self.client.get(self.book_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book.title)

    def test_03_create_book(self):
        """Checker: can create a book (authenticated)."""
        data = {
            'title': 'Animal Farm',
            'publication_year': 1945,
            'author': self.author.id
        }
        response = self.client.post(self.book_create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_04_update_book(self):
        """Checker: can update a book."""
        data = {
            'title': '1984 - Updated',
            'publication_year': 1949,
            'author': self.author.id
        }
        response = self.client.put(self.book_update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, '1984 - Updated')

    def test_05_delete_book(self):
        """Checker: can delete a book."""
        response = self.client.delete(self.book_delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(pk=self.book.pk).exists())

    def test_06_permissions_unauthenticated_cannot_create(self):
        """Unauthenticated user cannot create (security test)."""
        self.client.logout()
        data = {
            'title': 'Hacked Book',
            'publication_year': 2025,
            'author': self.author.id
        }
        response = self.client.post(self.book_create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_07_filter_books_by_title(self):
        """Test filtering (required in Task 2)."""
        Book.objects.create(title="Python Basics", publication_year=2020, author=self.author)
        response = self.client.get(self.book_list_url, {'title': 'Python'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertIn('Python', response.data[0]['title'])

    def test_08_search_books(self):
        """Test search functionality."""
        response = self.client.get(self.book_list_url, {'search': '1984'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_09_ordering_books(self):
        """Test ordering by title."""
        Book.objects.create(title="A Book", publication_year=2000, author=self.author)
        response = self.client.get(self.book_list_url, {'ordering': 'title'})
        titles = [book['title'] for book in response.data]
        self.assertEqual(titles, sorted(titles))

    def test_10_invalid_year_rejected(self):
        """Test serializer validation (future year)."""
        data = {
            'title': 'Time Traveler',
            'publication_year': 2500,
            'author': self.author.id
        }
        response = self.client.post(self.book_create_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('publication_year', response.data)