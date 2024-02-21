from ctypes import LibraryLoader  # Import necessary libraries
import tkinter as tk
from tkinter import messagebox, simpledialog, Entry
import csv
import uuid

class Library:
    def __init__(self):
        self.books = []  # Initialize empty lists for books, readers, and loans
        self.readers = []
        self.loans = []

    def add_book(self, title, author, year):  # Method to add a book to the library
        book_id = uuid.uuid4()  # Generate a unique ID for the book
        self.books.append({'id': book_id, 'title': title, 'author': author, 'year': year})  # Add book details to the list
        return book_id  # Return the ID of the added book

    def add_reader(self, name, contact):  # Method to add a reader to the library
        reader_id = uuid.uuid4()  # Generate a unique ID for the reader
        self.readers.append({'id': reader_id, 'name': name, 'contact': contact})  # Add reader details to the list
        return reader_id  # Return the ID of the added reader

    def view_books(self):  # Method to view all books in the library
        for book in self.books:  # Iterate through each book
            print(book)  # Print book details

    def view_readers(self):  # Method to view all readers in the library
        for reader in self.readers:  # Iterate through each reader
            print(reader)  # Print reader details

    def modify_book(self, book_id, title, author, year):  # Method to modify book details
        for book in self.books:  # Iterate through each book
            if book['id'] == book_id:  # Check if the book ID matches the provided ID
                book['title'] = title  # Update book title
                book['author'] = author  # Update book author
                book['year'] = year  # Update publication year

    def modify_reader(self, reader_id, name, contact):  # Method to modify reader details
        for reader in self.readers:  # Iterate through each reader
            if reader['id'] == reader_id:  # Check if the reader ID matches the provided ID
                reader['name'] = name  # Update reader name
                reader['contact'] = contact  # Update reader contact information

    def delete_book(self, book_id):  # Method to delete a book from the library
        self.books = [book for book in self.books if book['id'] != book_id]  # Remove the book with the provided ID

    def delete_reader(self, reader_id):  # Method to delete a reader from the library
        self.readers = [reader for reader in self.readers if reader['id'] != reader_id]  # Remove the reader with the provided ID

    def loan_book(self, book_id, reader_id):  # Method to loan a book to a reader
        loan_id = uuid.uuid4()  # Generate a unique ID for the loan
        self.loans.append({'id': loan_id, 'book_id': book_id, 'reader_id': reader_id})  # Add loan details to the list
        return loan_id  # Return the ID of the loan

    def return_book(self, loan_id):  # Method to return a book loan
        self.loans = [loan for loan in self.loans if loan['id'] != loan_id]  # Remove the loan with the provided ID

    def save_data(self):  # Method to save library data to CSV files
        with open('books.csv', 'w', newline='') as csvfile:  # Open CSV file for books
            writer = csv.DictWriter(csvfile, fieldnames=['id', 'title', 'author', 'year'])  # Create CSV writer
            writer.writeheader()  # Write CSV header
            writer.writerows(self.books)  # Write book data to CSV

        with open('readers.csv', 'w', newline='') as csvfile:  # Open CSV file for readers
            writer = csv.DictWriter(csvfile, fieldnames=['id', 'name', 'contact'])  # Create CSV writer
            writer.writeheader()  # Write CSV header
            writer.writerows(self.readers)  # Write reader data to CSV

    def load_data(self):  # Method to load library data from CSV files
        try:
            with open('books.csv', newline='') as csvfile:  # Open CSV file for books
                reader = csv.DictReader(csvfile)  # Create CSV reader
                self.books = list(reader)  # Read book data from CSV
        except FileNotFoundError:
            pass  # Ignore if file not found

        try:
            with open('readers.csv', newline='') as csvfile:  # Open CSV file for readers
                reader = csv.DictReader(csvfile)  # Create CSV reader
                self.readers = list(reader)  # Read reader data from CSV
        except FileNotFoundError:
            pass  # Ignore if file not found

        try:
            with open('loans.csv', newline='') as csvfile:  # Open CSV file for loans
                reader = csv.DictReader(csvfile)  # Create CSV reader
                self.loans = list(reader)  # Read loan data from CSV
        except FileNotFoundError:
            pass  # Ignore if file not found

library = Library()  # Create Library instance

def refresh_books_listbox():  # Function to refresh books listbox
    books_listbox.delete(0, tk.END)  # Clear existing items in the listbox
    for book in library.books:  # Iterate through each book in the library
        books_listbox.insert(tk.END, f"{book['title']} by {book['author']} ({book['year']})")  # Add book details to the listbox

def refresh_readers_listbox():  # Function to refresh readers listbox
    readers_listbox.delete(0, tk.END)  # Clear existing items in the listbox
    for reader in library.readers:  # Iterate through each reader in the library
        readers_listbox.insert(tk.END, f"{reader['name']} - {reader['contact']}")  # Add reader details to the listbox

root = tk.Tk()  # Create Tkinter root window

# Create book entry fields
tk.Label(root, text="Book Title").grid(row=0)  # Label for book title entry
tk.Label(root, text="Author").grid(row=1)  # Label for author entry
tk.Label(root, text="Publication Year").grid(row=2)  # Label for publication year entry

title_entry = tk.Entry(root)  # Entry field for book title
author_entry = tk.Entry(root)  # Entry field for author
year_entry = tk.Entry(root)  # Entry field for publication year

title_entry.grid(row=0, column=1)  # Position book title entry
author_entry.grid(row=1, column=1)  # Position author entry
year_entry.grid(row=2, column=1)  # Position publication year entry

# Create reader entry fields
tk.Label(root, text="Reader Name").grid(row=3)  # Label for reader name entry
tk.Label(root, text="Contact Info").grid(row=4)  # Label for contact info entry

name_entry = tk.Entry(root)  # Entry field for reader name
contact_entry = tk.Entry(root)  # Entry field for contact info

name_entry.grid(row=3, column=1)  # Position reader name entry
contact_entry.grid(row=4, column=1)  # Position contact info entry

# Function to handle adding a book
def add_book():  
    title = title_entry.get()  # Get title from entry field
    author = author_entry.get()  # Get author from entry field
    year = year_entry.get()  # Get year from entry field
    if title and author and year:  # Check if all fields are filled
        book_id = library.add_book(title, author, year)  # Add book to library
        refresh_books_listbox()  # Refresh books listbox
        messagebox.showinfo("Success", "Book added successfully.")  # Show success message
    else:
        messagebox.showerror("Error", "Please fill in all fields.")  # Show error message if fields are missing

# Function to handle adding a reader
def add_reader():  
    name = name_entry.get()  # Get name from entry field
    contact = contact_entry.get()  # Get contact from entry field
    if name and contact:  # Check if all fields are filled
        reader_id = library.add_reader(name, contact)  # Add reader to library
        refresh_readers_listbox()  # Refresh readers listbox
        messagebox.showinfo("Success", "Reader added successfully.")  # Show success message
    else:
        messagebox.showerror("Error", "Please fill in all fields.")  # Show error message if fields are missing

# Function to handle modifying a book
def modify_book():  
    selected_book = books_listbox.curselection()  # Get the index of the selected book
    if selected_book:  # Check if a book is selected
        title = title_entry.get()  # Get new title from entry field
        author = author_entry.get()  # Get new author from entry field
        year = year_entry.get()  # Get new year from entry field
        if title and author and year:  # Check if all fields are filled
            book_index = selected_book[0]  # Get the index of the selected book
            book_id = library.books[book_index]['id']  # Get the ID of the selected book
            library.modify_book(book_id, title, author, year)  # Modify book details
            refresh_books_listbox()  # Refresh books listbox
            messagebox.showinfo("Success", "Book modified successfully.")  # Show success message
        else:
            messagebox.showerror("Error", "Please fill in all fields.")  # Show error message if fields are missing
    else:
        messagebox.showerror("Error", "Please select a book to modify.")  # Show error message if no book is selected

# Function to handle deleting a book
def delete_book():  
    selected_book = books_listbox.curselection()  # Get the index of the selected book
    if selected_book:  # Check if a book is selected
        book_index = selected_book[0]  # Get the index of the selected book
        book_id = library.books[book_index]['id']  # Get the ID of the selected book
        library.delete_book(book_id)  # Delete book from library
        refresh_books_listbox()  # Refresh books listbox
        messagebox.showinfo("Success", "Book deleted successfully.")  # Show success message
    else:
        messagebox.showerror("Error", "Please select a book to delete.")  # Show error message if no book is selected

# Function to handle modifying a reader
def modify_reader():  
    selected_reader = readers_listbox.curselection()  # Get the index of the selected reader
    if selected_reader:  # Check if a reader is selected
        name = name_entry.get()  # Get new name from entry field
        contact = contact_entry.get()  # Get new contact from entry field
        if name and contact:  # Check if all fields are filled
            reader_index = selected_reader[0]  # Get the index of the selected reader
            reader_id = library.readers[reader_index]['id']  # Get the ID of the selected reader
            library.modify_reader(reader_id, name, contact)  # Modify reader details
            refresh_readers_listbox()  # Refresh readers listbox
            messagebox.showinfo("Success", "Reader modified successfully.")  # Show success message
        else:
            messagebox.showerror("Error", "Please fill in all fields.")  # Show error message if fields are missing
    else:
        messagebox.showerror("Error", "Please select a reader to modify.")  # Show error message if no reader is selected

# Function to handle deleting a reader
def delete_reader():  
    selected_reader = readers_listbox.curselection()  # Get the index of the selected reader
    if selected_reader:  # Check if a reader is selected
        reader_index = selected_reader[0]  # Get the index of the selected reader
        reader_id = library.readers[reader_index]['id']  # Get the ID of the selected reader
        library.delete_reader(reader_id)  # Delete reader from library
        refresh_readers_listbox()  # Refresh readers listbox
        messagebox.showinfo("Success", "Reader deleted successfully.")  # Show success message
    else:
        messagebox.showerror("Error", "Please select a reader to delete.")  # Show error message if no reader is selected

# Create buttons to add book and reader
tk.Button(root, text='Add Book', command=add_book).grid(row=5, column=0, sticky=tk.W, pady=4)  # Button to add book
tk.Button(root, text='Add Reader', command=add_reader).grid(row=5, column=1, sticky=tk.W, pady=4)  # Button to add reader

# Create listboxes to display books and readers
books_listbox = tk.Listbox(root)  # Listbox for books
readers_listbox = tk.Listbox(root)  # Listbox for readers

books_listbox.grid(row=6, column=0)  # Position books listbox
readers_listbox.grid(row=6, column=1)  # Position readers listbox

# Refresh books and readers listboxes
refresh_books_listbox()
refresh_readers_listbox()

# Create buttons to modify and delete books and readers
tk.Button(root, text='Modify Book', command=modify_book).grid(row=7, column=0, sticky=tk.W, pady=4)  # Button to modify book
tk.Button(root, text='Delete Book', command=delete_book).grid(row=7, column=1, sticky=tk.W, pady=4)  # Button to delete book
tk.Button(root, text='Modify Reader', command=modify_reader).grid(row=8, column=0, sticky=tk.W, pady=4)  # Button to modify reader
tk.Button(root, text='Delete Reader', command=delete_reader).grid(row=8, column=1, sticky=tk.W, pady=4)  # Button to delete reader

root.mainloop()  # Start Tkinter event loop






