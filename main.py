import os


class Library:
    def __init__(self, books_file='books.txt'):
        self.books_file = books_file
        if os.path.exists(books_file):
            with open(books_file, 'r') as f:
                self.books = [eval(line) for line in f.readlines()]
        else:
            self.books = []

    def display_books(self):
        print("List of books:")
        for index, book in enumerate(self.books):
            print(
                f"{index + 1}. Title: {book['title']} | Author: {book['author']} | ISBN: {book['ISBN']}")

    def add_book(self, title, author, ISBN):
        book = {
            "title": title,
            "author": author,
            "ISBN": ISBN
        }
        self.books.append(book)
        with open(self.books_file, 'a') as f:
            f.write(f"{book}\n")
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


def menu():
    print("Library Management System")
    print("1. Display books")
    print("2. Add book")
    print("3. Search book")
    print("4. Quit")


if __name__ == "__main__":
    library = Library()
    while True:
        menu()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            library.display_books()
        elif choice == 2:
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            ISBN = input("Enter book ISBN: ")
            library.add_book(title, author, ISBN)
        elif choice == 3:
            search_type = int(
                input("Search by:\n1. Title\n2. Author\n3. ISBN\nEnter your choice: "))
            if search_type == 1:
                title = input("Enter book title: ")
                books = library.search_book(title=title)
            elif search_type == 2:
                author = input("Enter book author: ")
                books = library.search_book(author=author)
            elif search_type == 3:
                ISBN = input("Enter book ISBN: ")
                books = library.search_book(ISBN=ISBN)
            else:
                print("Quitting Library Management System...")
                break

if books:
    for book in books:
        print(
            f"Title: {book['title']} | Author: {book['author']} | ISBN: {book['ISBN']}")
else:
    print("No books found.")
