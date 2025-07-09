from bookshelf.models import Book

# Command

book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Output (example)

# <Book: 1984 by George Orwell (1949)>
