# library_system.py

class Book:
    """
    Base class representing a generic book.
    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        year (int): The publication year of the book.
    """
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year
        # Removed "Book ... has been created." message as it's not in expected output

    def __str__(self):
        """
        Returns a human-readable string representation of the Book object.
        Matches the format: "TITLE by AUTHOR, published in YEAR"
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Returns the official string representation of the Book object,
        allowing it to be unambiguously recreated.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        """
        Destructor method called when the Book object is about to be destroyed.
        Matches the format: "Deleting TITLE"
        """
        print(f"Deleting {self.title}")


class EBook(Book):
    """
    Derived class representing an electronic book, inheriting from Book.
    Additional Attributes:
        file_size (int): The size of the e-book file in KB.
    """
    def __init__(self, title: str, author: str, year: int, file_size: int):
        # Call the constructor of the base class (Book)
        super().__init__(title, author, year)
        self.file_size = file_size

    def __str__(self):
        """
        Returns a human-readable string representation of the EBook object.
        Overrides the __str__ method from the base Book class.
        """
        return f"EBook: {self.title} by {self.author} ({self.year}), File Size: {self.file_size}KB"

    def __repr__(self):
        """
        Returns the official string representation of the EBook object.
        """
        return f"EBook('{self.title}', '{self.author}', {self.year}, {self.file_size})"

    def __del__(self):
        """
        Destructor method called when the EBook object is about to be destroyed.
        """
        # Adjusted for consistency with the base Book's __del__
        print(f"Deleting {self.title}")


class PrintBook(Book):
    """
    Derived class representing a print book, inheriting from Book.
    Additional Attributes:
        page_count (int): The number of pages in the print book.
    """
    def __init__(self, title: str, author: str, year: int, page_count: int):
        # Call the constructor of the base class (Book)
        super().__init__(title, author, year)
        self.page_count = page_count

    def __str__(self):
        """
        Returns a human-readable string representation of the PrintBook object.
        Overrides the __str__ method from the base Book class.
        """
        return f"PrintBook: {self.title} by {self.author} ({self.year}), Page Count: {self.page_count}"

    def __repr__(self):
        """
        Returns the official string representation of the PrintBook object.
        """
        return f"PrintBook('{self.title}', '{self.author}', {self.year}, {self.page_count})"

    def __del__(self):
        """
        Destructor method called when the PrintBook object is about to be destroyed.
        """
        # Adjusted for consistency with the base Book's __del__
        print(f"Deleting {self.title}")


class Library:
    """
    Represents a library that manages a collection of books.
    Demonstrates composition, as it 'has a' list of Book objects.
    Attributes:
        books (list): A list to store instances of Book, EBook, and PrintBook.
    """
    def __init__(self):
        self.books = [] # Initialize an empty list to hold book objects
        # Removed "Library instance created." message as it's not in expected output

    def add_book(self, book: Book):
        """
        Adds a book (can be Book, EBook, or PrintBook instance) to the library's collection.
        Args:
            book (Book): An instance of Book or its subclasses.
        """
        if isinstance(book, Book):
            self.books.append(book)
            print(f"Added '{book.title}' to the library.")
        else:
            print(f"Error: Cannot add non-Book object to the library.")

    def list_books(self):
        """
        Prints the details of each book currently in the library's collection.
        Leverages the __str__ method of each book object for formatted output.
        """
        print("\n--- Books in the Library ---")
        if not self.books:
            print("The library is currently empty.")
            return

        for book in self.books:
            print(book) # This will automatically call the appropriate __str__ method
        print("--- End of Book List ---")
