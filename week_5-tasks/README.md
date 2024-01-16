                                      Library Management System Project
This Python-based Library Management System is designed to efficiently manage a library's collection of books and user transactions. The project is organized into classes to represent books, users, the library itself, and transactions. Below is an overview of each class and its functionalities:

Book Class:
The Book class represents individual books in the library with the following attributes:

title: Title of the book.
author: Author of the book.
ISBN: International Standard Book Number for identification.
availability_status: Availability status of the book (default is True).
Implemented methods:

display_details(): Displays detailed information about the book.
update_availability(new_status): Updates the availability status of the book.
User Class:
The User class represents library users with the following attributes:

user_id: Unique identifier for each user.
name: Name of the user.
books_borrowed: List of books borrowed by the user.
Implemented methods:

display_user_details(): Displays detailed information about the user.
borrow_book(book): Allows the user to borrow a book.
return_book(book): Allows the user to return a book.
Library Class:
The Library class manages the overall collection of books and user information with the following attributes:

books_collection: List to store all books in the library.
registered_users: List to store information about registered users.
Implemented methods:

add_book(book): Adds a new book to the library.
register_user(user): Registers a new user with the library.
display_books_in_library(): Displays details of all books in the library.
display_registered_users(): Displays details of all registered users.
book_transaction(user, book, transaction_type): Handles book transactions such as borrowing and returning.
Transaction Class:
The Transaction class represents book transactions, including borrowing and returning, with the following attribute:

transactions: List to store transaction records.
Implemented methods:

record_transaction(user, book, transaction_type): Records a book transaction.
generate_transaction_report(): Generates a transaction report.
