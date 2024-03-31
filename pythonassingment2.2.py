from datetime import datetime, timedelta

class LibrarySystem:
    def __init__(self):
        self.catalog = {
            1: {'title': 'Book1', 'author': 'Author1', 'quantity': 5},
            2: {'title': 'Book2', 'author': 'Author2', 'quantity': 3},
            # Add more books as needed
        }
        self.users = {}
        self.transactions = {}

    def display_catalog(self):
        print("\nLibrary Catalog:")
        for book_id, book_info in self.catalog.items():
            availability = book_info['quantity']
            print(f"ID: {book_id}, Title: {book_info['title']}, Author: {book_info['author']}, Available: {availability}")

    def register_user(self, user_id, name):
        self.users[user_id] = {'name': name, 'checked_out_books': {}}

    def checkout_book(self, user_id, book_id):
        if user_id not in self.users:
            print("User not registered. Please register first.")
            return

        if book_id not in self.catalog:
            print("Invalid book ID. Please enter a valid ID.")
            return

        if self.catalog[book_id]['quantity'] == 0:
            print("Book not available for checkout.")
            return

        user_checked_out_books = self.users[user_id]['checked_out_books']
        if len(user_checked_out_books) >= 3:
            print("Maximum limit of 3 books reached. Return a book to checkout another.")
            return

        checkout_date = datetime.now()
        due_date = checkout_date + timedelta(days=14)

        user_checked_out_books[book_id] = {'checkout_date': checkout_date, 'due_date': due_date}
        self.catalog[book_id]['quantity'] -= 1

        transaction_id = len(self.transactions) + 1
        self.transactions[transaction_id] = {'user_id': user_id, 'book_id': book_id, 'checkout_date': checkout_date}

        print(f"Book '{self.catalog[book_id]['title']}' checked out successfully. Due date: {due_date}")

    def return_book(self, user_id, book_id):
        if user_id not in self.users:
            print("User not registered. Please register first.")
            return

        if book_id not in self.catalog:
            print("Invalid book ID. Please enter a valid ID.")
            return

        user_checked_out_books = self.users[user_id]['checked_out_books']
        if book_id not in user_checked_out_books:
            print("Book not checked out by this user.")
            return

        checkout_date = user_checked_out_books[book_id]['checkout_date']
        due_date = user_checked_out_books[book_id]['due_date']
        return_date = datetime.now()

        overdue_days = max(0, (return_date - due_date).days)
        overdue_fine = overdue_days * 1  # $1 per day overdue

        self.catalog[book_id]['quantity'] += 1
        del user_checked_out_books[book_id]

        transaction_id = len(self.transactions) + 1
        self.transactions[transaction_id] = {'user_id': user_id, 'book_id': book_id, 'return_date': return_date,
                                              'overdue_days': overdue_days, 'overdue_fine': overdue_fine}

        print(f"Book '{self.catalog[book_id]['title']}' returned successfully.")

        if overdue_days > 0:
            print(f"Overdue fine: ${overdue_fine}")

    def list_overdue_books(self, user_id):
        if user_id not in self.users:
            print("User not registered. Please register first.")
            return

        user_checked_out_books = self.users[user_id]['checked_out_books']
        overdue_books = [(book_id, info) for book_id, info in user_checked_out_books.items() if datetime.now() > info['due_date']]

        if not overdue_books:
            print("No overdue books for this user.")
            return

        total_fine = sum(info['overdue_fine'] for _, info in overdue_books)
        print("\nOverdue Books:")
        for book_id, info in overdue_books:
            print(f"Book ID: {book_id}, Title: {self.catalog[book_id]['title']}, Overdue Days: {info['overdue_days']}, Fine: ${info['overdue_fine']}")

        print(f"Total Fine Due: ${total_fine}")

    # Additional Features
    def add_book_to_catalog(self, book_id, title, author, quantity):
        if book_id in self.catalog:
            print("Book ID already exists. Please use a different ID.")
            return

        self.catalog[book_id] = {'title': title, 'author': author, 'quantity': quantity}
        print(f"Book '{title}' added to the catalog successfully.")

    def remove_book_from_catalog(self, book_id):
        if book_id not in self.catalog:
            print("Invalid book ID. Please enter a valid ID.")
            return

        del self.catalog[book_id]
        print("Book removed from the catalog successfully.")

    def extend_due_date(self, user_id, book_id):
        if user_id not in self.users:
            print("User not registered. Please register first.")
            return

        user_checked_out_books = self.users[user_id]['checked_out_books']
        if book_id not in user_checked_out_books:
            print("Book not checked out by this user.")
            return

        if 'due_date_extension' in user_checked_out_books[book_id]:
            print("Due date can be extended only once per checkout.")
            return

        user_checked_out_books[book_id]['due_date'] += timedelta(days=7)
        user_checked_out_books[book_id]['due_date_extension'] = True
        print(f"Due date for Book '{self.catalog[book_id]['title']}' extended by 7 days.")

# Example Usage:
library = LibrarySystem()

# User Registration
library.register_user(1, 'John Doe')

# Display Catalog
library.display_catalog()

# Checkout Book
library.checkout_book(1, 1)

# Return Book
library.return_book(1, 1)

# List Overdue Books
library.list_overdue_books(1)

# Additional Features
library.add_book_to_catalog(3, 'Book3', 'Author3', 2)
library.remove_book_from_catalog(2)
library.extend_due_date(1, 1)

# Class Definition: LibrarySystem
# The script starts by defining a class called LibrarySystem to encapsulate the functionality of the library management system. Here's a breakdown of the key methods:

# __init__(self): The class constructor initializes the system with a predefined catalog, an empty user registry, and an empty list of transactions.

# display_catalog(self): This method displays the current catalog of books, including their IDs, titles, authors, and availability status.

# register_user(self, user_id, name): Registers a new user with a unique ID and a name.

# checkout_book(self, user_id, book_id): Allows a user to check out a book by specifying the user ID and the book ID. It records the checkout date and updates the catalog and transactions accordingly.

# return_book(self, user_id, book_id): Handles the return of a book, updating the catalog and transactions. If the book is returned after the due date, it calculates and prints the overdue fine.

# list_overdue_books(self, user_id): Lists all overdue books for a particular user along with the total fine due.

# display_transactions(self): Displays a list of transactions (books checked out or returned) in the system.

# 2. CLI for Library System: library_cli()
# The script includes a simple command-line interface (CLI) function named library_cli() to interact with the library management system. Here's how it works:

# Inside the while True loop, the user is presented with a menu displaying various options.

# Based on the user's choice (1-7), corresponding methods of the LibrarySystem class are invoked.

# The CLI continues to run until the user chooses the "Exit" option.

# 3. Example Usage
# The script concludes with an example usage of the LibrarySystem and the CLI. This includes displaying the catalog, registering a user, checking out books, returning a book, listing overdue books, and displaying transactions.

# Notes:
# The script uses basic data structures such as dictionaries and lists to manage information about books, users, and transactions.

# The script is designed for simplicity and may need further enhancements based on specific requirements