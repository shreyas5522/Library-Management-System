class Library:
    def __init__(self, books=[]):
        self.books = books

    def display_books(self):
        print("List of books:")
        for book in self.books:
            print(f"Title: {book['title']} | Author: {book['author']} | ISBN: {book['ISBN']}")

    def add_book(self, title, author, ISBN):
        book = {
            "title": title,
            "author": author,
            "ISBN": ISBN
        }
        self.books.append(book)
        print(f"Book '{title}' by {author} has been added to the library.")

    def search_book(self, title=None, author=None, ISBN=None):
        found_books = []
        for book in self.books:
            if title and book['title'] == title:
                found_books.append(book)
            elif author and book['author'] == author:
                found_books.append(book)
            elif ISBN and book['ISBN'] == ISBN:
                found_books.append(book)
        if found_books:
            return found_books
        else:
            print("No books found.")

if __name__ == "__main__":
    library = Library()
    library.add_book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", "0-345-39180-2")
    library.add_book("To Kill a Mockingbird", "Harper Lee", "0-449-94970-8")
    library.display_books()
    books = library.search_book(author="Douglas Adams")
    print("Books by Douglas Adams:")
    for book in books:
        print(f"Title: {book['title']} | ISBN: {book['ISBN']}")
