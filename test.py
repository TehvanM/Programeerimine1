import os
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
        desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        books_file_path = os.path.join(desktop_path, 'books.csv')
        readers_file_path = os.path.join(desktop_path, 'readers.csv')

        with open(books_file_path, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['id', 'title', 'author', 'year'])
            writer.writeheader()
            writer.writerows(self.books)

        with open(readers_file_path, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['id', 'name', 'contact'])
            writer.writeheader()
            writer.writerows(self.readers)

    def load_data(self):
        # Load data from files as before
        pass

library = Library()

def salvesta_csv_failid():
    library.save_data()
    messagebox.showinfo("Success", "CSV files saved successfully to Desktop.")

root = tk.Tk()

tk.Button(root, text='Save CSV Files', command=salvesta_csv_failid).grid(row=0, column=0, sticky=tk.W, pady=4)

root.mainloop()