class Book:
    def __init__(self, title, author, availability=True):  # Default availability
        self.title = title
        self.author = author
        self.availability = availability

    def borrowBook(self):
        if self.availability:
            self.availability = False
            print(f'"{self.title}" borrowed.')
        else:
            print(f'"{self.title}" is currently not available.')

    def returnBook(self):
        if self.availability:
            print(f'"{self.title}" is already in the library.')
        else:
            self.availability = True
            print(f'"{self.title}" returned.')

    def checkAvailability(self):
        print(f"Book Title: {self.title}")
        print(f"Book Author: {self.author}")
        print(f"Book Status: {'Available' if self.availability else 'Not Available'}")
        print("-" * 40)


class Library:
    def __init__(self):
        self.books = []

    def addBook(self):
        print("====== Adding new Book ====== ")
        title = input("Enter the Book Title: ")
        author = input("Enter Book's Author: ")
        newBook = Book(title, author)
        self.books.append(newBook)
        print("Book Added!")

    def borrowBook(self):
        title = input("Enter the title of the book you want to borrow: ")
        for book in self.books:
            if book.title.lower() == title.lower():
                book.borrowBook()
                return
        print("Book not found in the library.")

    def returnBook(self):
        title = input("Enter the title of the book you want to return: ")
        for book in self.books:
            if book.title.lower() == title.lower():
                book.returnBook()
                return
        print("Book not found in the library.")

    def viewBooks(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("====== Library Book List ======")
            for book in self.books:
                book.checkAvailability()


def menu():
    print("==============================")
    print("1. Add Book")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. View Books")
    print("5. Exit")
    print("==============================")


def main():
    library = Library()

    choice = ""
    while choice != "5":
        menu()
        choice = input("Select an option: ").lower()
        if choice == "1":
            library.addBook()
        elif choice == "2":
            library.borrowBook()
        elif choice == "3":
            library.returnBook()
        elif choice == "4":
            library.viewBooks()
        elif choice == "5":
            print("Exiting. See you soon...")
        else:
            print("Invalid input. Try again.")

main()