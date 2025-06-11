class Book:
    def __init__(self, title, author, availability):
        self.title = title
        self.author = author
        self.availability = availability
        
    def borrowBook(self):
        if self.availability:
            self.availability = False
            print (f'"{self.title}" borrowed.')
        else:
            print (f'"{self.title}" is currently not available.')
        
    def returnBook(self):
        if self.availability:
            print (f'"{self.title}" is already in the library.')
        else:
            self.availability = True
            print (f'"{self.title}" returned.')
        
    def checkAvailability(self):
        print (f"Book Title: {self.title}")
        print (f"Book Author: {self.author}")
        if self.availability:
            print (f"Book Status: Available")
        else:
            print (f"Book Status: Not Available")
        
class Library:
    def __init__(self):
        self.books = []
    
    def addBook(self):
        print ("====== Adding new Book ====== ")
        title = input("Enter the Book Title: ")
        author = input("Enter Book's Author: ")
        newBook = Book(title, author)
        self.books.append(newBook)
        print ("Book Added!")
    
    def borrowBook(self):
        title = input("Enter the title of the book you want to borrow: ")
        for book in self.books:
            if book.title.lower() == title.lower():
                book.borrowBook()
                return
            else:
                print("Book not found in the library.")
    
    def returnBook(self):
        return
    
    def viewBooks(self):
        return
    
def menu():
    print("==============================")
    print("1. Add Book")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. View Books")
    print("5. Exit")
    print("==============================")

def main():
    
    choice=0
    while (choice!="5"):
        menu()
        choice = input("Select an option: ").lower()
        if choice=="1":
           Library.addBook()
        elif choice=="2":
           Library.borrowBook()
        elif choice == "3":
           Library.returnBook()
        elif choice == "4":
           Library.viewBooks()
        elif choice == "5":
            print("Exiting. See you soon...")
        else:
            print("")
            print("Invalid input. Try again.")
            
main()