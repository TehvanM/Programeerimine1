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

def open_csv_files():  # Function to open CSV files and refresh listboxes
    library.load_data()  # Load data from CSV files
    refresh_books_listbox()  # Refresh books listbox
    refresh_readers_listbox()  # Refresh readers listbox
    messagebox.showinfo("Success", "CSV files opened successfully.")  # Show success message

def add_book():  
    title = title_entry.get()  
    author = author_entry.get()  
    year = year_entry.get()  
    if title and author and year:  
        book_id = library.add_book(title, author, year)  
        refresh_books_listbox()  
        messagebox.showinfo("Success", "Book added successfully.")  
    else:
        messagebox.showerror("Error", "Please fill in all fields.")  

def add_reader():  
    name = name_entry.get()  
    contact = contact_entry.get()  
    if name and contact:  
        reader_id = library.add_reader(name, contact)  
        refresh_readers_listbox()  
        messagebox.showinfo("Success", "Reader added successfully.")  
    else:
        messagebox.showerror("Error", "Please fill in all fields.")  

root = tk.Tk()  # Create Tkinter root window

# Add button to import CSV files
tk.Button(root, text='Open CSV Files', command=open_csv_files).grid(row=0, column=0, sticky=tk.W, pady=4)

books_listbox = tk.Listbox(root)
readers_listbox = tk.Listbox(root)

books_listbox.grid(row=1, column=0)
readers_listbox.grid(row=1, column=1)

# Create book entry fields
tk.Label(root, text="Book Title").grid(row=2)  # Label for book title entry
tk.Label(root, text="Author").grid(row=3)  # Label for author entry
tk.Label(root, text="Publication Year").grid(row=4)  # Label for publication year entry

title_entry = tk.Entry(root)  # Entry field for book title
author_entry = tk.Entry(root)  # Entry field for author
year_entry = tk.Entry(root)  # Entry field for publication year

title_entry.grid(row=2, column=1)  # Position book title entry
author_entry.grid(row=3, column=1)  # Position author entry
year_entry.grid(row=4, column=1)  # Position publication year entry

# Create reader entry fields
tk.Label(root, text="Reader Name").grid(row=5)  # Label for reader name entry
tk.Label(root, text="Contact Info").grid(row=6)  # Label for contact info entry

name_entry = tk.Entry(root)  # Entry field for reader name
contact_entry = tk.Entry(root)  # Entry field for contact info

name_entry.grid(row=5, column=1)  # Position reader name entry
contact_entry.grid(row=6, column=1)  # Position contact info entry

# Create buttons to add book and reader
tk.Button(root, text='Add Book', command=add_book).grid(row=7, column=0, sticky=tk.W, pady=4)  # Button to add book
tk.Button(root, text='Add Reader', command=add_reader).grid(row=7, column=1, sticky=tk.W, pady=4)  # Button to add reader

root.mainloop()  # Start Tkinter event loop