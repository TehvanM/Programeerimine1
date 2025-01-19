import tkinter as tk
from tkinter import messagebox
import csv
import uuid

class Library:
    def __init__(self):
        self.books = []
        self.readers = []
        self.loans = []

    def add_book(self, title, author, year):
        book_id = uuid.uuid4()
        self.books.append({'id': book_id, 'title': title, 'author': author, 'year': year})
        return book_id

    def add_reader(self, name, contact):
        reader_id = uuid.uuid4()
        self.readers.append({'id': reader_id, 'name': name, 'contact': contact})
        return reader_id

    def modify_book(self, book_id, title, author, year):
        for book in self.books:
            if book['id'] == book_id:
                book['title'] = title
                book['author'] = author
                book['year'] = year

    def modify_reader(self, reader_id, name, contact):
        for reader in self.readers:
            if reader['id'] == reader_id:
                reader['name'] = name
                reader['contact'] = contact

    def delete_book(self, book_id):
        self.books = [book for book in self.books if book['id'] != book_id]

    def delete_reader(self, reader_id):
        self.readers = [reader for reader in self.readers if reader['id'] != reader_id]

    def save_data(self):
        with open('books.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['id', 'title', 'author', 'year'])
            writer.writeheader()
            writer.writerows(self.books)

        with open('readers.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['id', 'name', 'contact'])
            writer.writeheader()
            writer.writerows(self.readers)

    def load_data(self):
        try:
            with open('books.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                self.books = list(reader)
        except FileNotFoundError:
            pass

        try:
            with open('readers.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                self.readers = list(reader)
        except FileNotFoundError:
            pass

library = Library()

def refresh_books_listbox():
    books_listbox.delete(0, tk.END)
    for book in library.books:
        books_listbox.insert(tk.END, f"{book['title']} by {book['author']} ({book['year']})")

def refresh_readers_listbox():
    readers_listbox.delete(0, tk.END)
    for reader in library.readers:
        readers_listbox.insert(tk.END, f"{reader['name']} - {reader['contact']}")

def open_csv_files():
    library.load_data()
    refresh_books_listbox()
    refresh_readers_listbox()
    messagebox.showinfo("Success", "CSV files opened successfully.")

root = tk.Tk()

tk.Button(root, text='Open CSV Files', command=open_csv_files).grid(row=0, column=0, sticky=tk.W, pady=4)

tk.Label(root, text="Book Title").grid(row=1)
tk.Label(root, text="Author").grid(row=2)
tk.Label(root, text="Publication Year").grid(row=3)

title_entry = tk.Entry(root)
author_entry = tk.Entry(root)
year_entry = tk.Entry(root)

title_entry.grid(row=1, column=1)
author_entry.grid(row=2, column=1)
year_entry.grid(row=3, column=1)

tk.Label(root, text="Reader Name").grid(row=4)
tk.Label(root, text="Contact Info").grid(row=5)

name_entry = tk.Entry(root)
contact_entry = tk.Entry(root)

name_entry.grid(row=4, column=1)
contact_entry.grid(row=5, column=1)

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

def modify_book():
    selected_book = books_listbox.curselection()
    if selected_book:
        title = title_entry.get()
        author = author_entry.get()
        year = year_entry.get()
        if title and author and year:
            book_index = selected_book[0]
            book_id = library.books[book_index]['id']
            library.modify_book(book_id, title, author, year)
            refresh_books_listbox()
            messagebox.showinfo("Success", "Book modified successfully.")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")
    else:
        messagebox.showerror("Error", "Please select a book to modify.")

def delete_book():
    selected_book = books_listbox.curselection()
    if selected_book:
        book_index = selected_book[0]
        book_id = library.books[book_index]['id']
        library.delete_book(book_id)
        refresh_books_listbox()
        messagebox.showinfo("Success", "Book deleted successfully.")
    else:
        messagebox.showerror("Error", "Please select a book to delete.")

def modify_reader():
    selected_reader = readers_listbox.curselection()
    if selected_reader:
        name = name_entry.get()
        contact = contact_entry.get()
        if name and contact:
            reader_index = selected_reader[0]
            reader_id = library.readers[reader_index]['id']
            library.modify_reader(reader_id, name, contact)
            refresh_readers_listbox()
            messagebox.showinfo("Success", "Reader modified successfully.")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")
    else:
        messagebox.showerror("Error", "Please select a reader to modify.")

def delete_reader():
    selected_reader = readers_listbox.curselection()
    if selected_reader:
        reader_index = selected_reader[0]
        reader_id = library.readers[reader_index]['id']
        library.delete_reader(reader_id)
        refresh_readers_listbox()
        messagebox.showinfo("Success", "Reader deleted successfully.")
    else:
        messagebox.showerror("Error", "Please select a reader to delete.")

tk.Button(root, text='Add Book', command=add_book).grid(row=6, column=0, sticky=tk.W, pady=4)
tk.Button(root, text='Add Reader', command=add_reader).grid(row=6, column=1, sticky=tk.W, pady=4)

books_listbox = tk.Listbox(root)
readers_listbox = tk.Listbox(root)

books_listbox.grid(row=7, column=0)
readers_listbox.grid(row=7, column=1)

refresh_books_listbox()
refresh_readers_listbox()

tk.Button(root, text='Modify Book', command=modify_book).grid(row=8, column=0, sticky=tk.W, pady=4)
tk.Button(root, text='Delete Book', command=delete_book).grid(row=8, column=1, sticky=tk.W, pady=4)
tk.Button(root, text='Modify Reader', command=modify_reader).grid(row=9, column=0, sticky=tk.W, pady=4)
tk.Button(root, text='Delete Reader', command=delete_reader).grid(row=9, column=1, sticky=tk.W, pady=4)

root.mainloop()
