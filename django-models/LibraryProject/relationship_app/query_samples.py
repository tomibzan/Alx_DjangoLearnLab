from relationship_app.models import Author, Book, Library, Librarian


def query_all_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        print(f"Books by {author_name}:")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"No author found with the name '{author_name}'")


def list_all_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"Books in {library_name}:")
        for book in books:
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print(f"No library found with the name '{library_name}'")


def retrieve_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian
        print(f"Librarian for {library_name}: {librarian.name}")
    except Library.DoesNotExist:
        print(f"No library found with the name '{library_name}'")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to {library_name}")


# Example usage:
if __name__ == "__main__":
    print("Querying all books by J.K. Rowling:")
    query_all_books_by_author("J.K. Rowling")

    print("\nListing all books in Central Library:")
    list_all_books_in_library("Central Library")

    print("\nRetrieving librarian for Central Library:")
    retrieve_librarian_for_library("Central Library")
