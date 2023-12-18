class Book:

    def __init__(self, title, author, ISBN, availablity_status )
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.availablity_status = availablity_status

    def display_book_details(self):
        print(f"Title: {self.title} Author: {self.author} ISBM: {self.ISBN} Available_status: {self.availablity_status} ")

    def update_availability_status(self, new_status)
        self.availablity_status = new_status
        print(f"availablity_status updated to {self.availablity_status} ")

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.books_borrowed = []

    def display_user_details(self):
       
        print(f"User ID: {self.user_id}")
        print(f"Name: {self.name}")
        print(f"Books Borrowed: {self.books_borrowed}")

    def borrow_book(self, book):
        
        self.books_borrowed.append(book)
        print(f"{self.name} has borrowed {book}")

    def return_book(self, book):
        
        if book in self.books_borrowed:
            self.books_borrowed.remove(book)
            print(f"{self.name} has returned {book}")
        else:
            print(f"{self.name} has not borrowed {book}")

class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.transactions = []

    def add_book(self, book):
        
        self.books.append(book)
        print(f"{book.title} added to the library")

    def register_user(self, user):

        self.users.append(user)
        print(f"{user.name} registered with the library")

    def borrow_book(self, user, book):
        
        if book in self.books:
            user.borrow_book(book.title)
            book.update_availability_status("Not Available")
            self.transactions.append(Transaction(user, book, "Borrowed"))
        else:
            print(f"{book.title} is not available in the library")

    def return_book(self, user: User, book: Book):
        
        if book in self.books:
            user.return_book(book.title)
            book.update_availability_status("Available")
            self.transactions.append(Transaction(user, book, "Returned"))
        else:
            print(f"{book.title} is not available in the library")

    def generate_transaction_report(self):
        
        for transaction in self.transactions:
            print(f"{transaction.user.name} {transaction.action} {transaction.book.title}")



class Transaction:
    def __init__(self):
        self.transactions = []

    def record_transaction(self, user, book, transaction_type):
        transaction_record = {
            "user": user.name,
            "book": book.title,
            "transaction_type": transaction_type,
        }
        self.transactions.append(transaction_record)

    def generate_transaction_report(self):
        print("Transaction Report:")
        for transaction in self.transactions:
            print(f"{transaction['user']} {transaction['transaction_type']}ed '{transaction['book']}'")
        print()