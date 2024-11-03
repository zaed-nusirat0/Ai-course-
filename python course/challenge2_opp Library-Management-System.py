'''
**Create a Library class to manage books and allow students to:**

1. **View available books**.
2. **Borrow a book** (the book should be removed from the available list if borrowed).
3. **Return a book** (adds the book back to the available list).

**Requirements:**

* Use a list attribute to store available books.
* Implement `display_books`, `borrow_book`, and `return_book` methods.
'''


from abc import ABC, abstractmethod

# Abstract base class for a Library
class Library(ABC):
    @abstractmethod
    def __init__(self, books=None):
        # Initialize the library with a list of books or an empty list if none provided
        self.__books = books if books else []

    @abstractmethod
    def display_books(self):
        # Abstract method to display all books
        pass

    @abstractmethod
    def borrow_book(self, remove_book):
        # Abstract method for borrowing a book
        pass

    @abstractmethod
    def return_book(self, book):
        # Abstract method for returning a book
        pass

# Concrete class for a library specific to Jordan University
class Library_jordan_university(Library):
    
    def __init__(self, books=None):
        # Call the superclass initializer and set up additional attributes
        super().__init__(books)
        self.__books = books if books else []
        self.count_books = 0  # Counter for tracking the total number of books
        self.history = []     # List to track borrow and return history

    def display_books(self):
        # Display all books in the library with an index
        for i, book in enumerate(self.__books, start=1):
            print(f"{i} - {book}")

    def borrow_book(self, remove_book):
        # Borrow a book if available, update count and history, else display a message
        if remove_book in self.__books:
            self.count_books = len(self.__books)  # Update book count
            self.history.append(f"borrow_book: -{remove_book}")  # Log action in history
            print(f"You have borrowed '{remove_book}'".title())
        else:
            print("Sorry, the requested book is not available in the library.")

    def return_book(self, book):
        # Return a book to the library, update count and history
        self.__books.append(book)  # Add book back to library
        self.count_books = len(self.__books)  # Update book count
        self.history.append(f"return_book: -{book}")  # Log action in history
        print(f"You have returned '{book}'".title())

    def search_books(self, book):
        # Search for a book and notify if available or not
        if book in self.__books:
            print(f"'{book}' is available in the library.".title())
        else:
            print(f"'{book}' is not in the library.".title())

    def update_books(self, new_books):
        # Replace the current book list with a new list if provided in correct format
        if isinstance(new_books, list):
            self.__books = new_books  # Update books list
            print("Books list has been updated.".title())
        else:
            print("Please provide a list of books.".title())

    def check_availability(self, book):
        # Check if a specific book is available in the library
        return book in self.__books

    def display_count_books(self):
        # Display the total number of books currently in the library
        print(f"Total number of books available in the library: {self.count_books}")

    def get_book_by_index(self, index):
        # Retrieve a book by its index; handle errors if index is invalid
        try:
            return f"The book {self.__books[index]}".title()
        except (IndexError, ValueError):
            print("Invalid index. Please provide an index within the range of available books.")

    def sort_books(self):
        # Sort the list of books alphabetically
        self.__books.sort()

    def track_borrowed_history(self):
        # Display the history of borrowed and returned books
        print(f"Track borrowed history : {self.history}".title())
# Define a list of books for the library upon creation
books_list = ["Data Science 101", "Python Programming", "Artificial Intelligence Basics", "Machine Learning Guide"]

# Create an instance of the Library_jordan_university class
library = Library_jordan_university(books_list)

# 1. Display all books in the library
print("Displaying all books in the library:")
library.display_books()

# 2. Borrow a book from the library
print("\nAttempting to borrow a book:")
library.borrow_book("Python Programming")

# 3. Return the borrowed book to the library
print("\nReturning the borrowed book:")
library.return_book("Python Programming")

# 4. Search for a specific book in the library
print("\nSearching for a specific book:")
library.search_books("Data Science 101")

# 5. Update the book list completely
print("\nUpdating the books list:")
new_books_list = ["Deep Learning Fundamentals", "Natural Language Processing"]
library.update_books(new_books_list)

# 6. Check availability of a specific book in the library
print("\nChecking availability of a book:")
is_available = library.check_availability("Deep Learning Fundamentals")
print(f"Is 'Deep Learning Fundamentals' available? {is_available}")

# 7. Display the current count of books in the library
print("\nDisplaying the current count of books in the library:")
library.display_count_books()

# 8. Get a book by its index in the list
print("\nGetting a book by its index:")
print(library.get_book_by_index(0))  # Get the first book

# 9. Sort the books alphabetically
print("\nSorting the books alphabetically:")
library.sort_books()
library.display_books()

# 10. Display the history of borrowed and returned books
print("\nDisplaying the borrowed and returned books history:")
library.track_borrowed_history()
