
# Raamatukogu laenutussĆ¼steemi arendamine

# EesmĆ¤rk: Luua Pythoni ja Tkinteri abil rakendus, mis haldab raamatukogu laenutustegevust. Rakendus vĆµimaldab kasutajatel sisestada, vaadata, muuta ja kustutada teavet laenutatud raamatute ja lugejate kohta. Iga laenutuse kohta genereeritakse sĆ¼steemi lisamisel unikaalne laenutus-ID.

# Funktsionaalsus:
# * Raamatute ja lugejate andmete sisestamine: Kasutajad saavad sisestada raamatute (pealkiri, autor, vĆ¤ljaandeaasta) ja lugejate (nimi, kontaktandmed) andmeid. Iga uue laenutuse puhul genereerib sĆ¼steem unikaalse laenutus-ID.
# * Laenutuste vaatamine: Rakendus kuvab kĆµik aktiivsed laenutused, sealhulgas raamatu pealkirja, autori, lugeja nime ja laenutusperioodi. Kasutajad saavad otsida laenutusi laenutus-ID, lugeja nime vĆµi raamatu pealkirja alusel.
# * Laenutuste muutmine ja kustutamine: Kasutajad saavad pikendada laenutusperioode, muuta lugeja kontaktandmeid vĆµi kustutada laenutusi sĆ¼steemist.
# * Andmete salvestamine: Andmed salvestatakse failisĆ¼steemi, kasutades CSV vĆµi TXT failivormingut, mis vĆµimaldab hĆµlpsat andmete haldamist ja taaskasutamist.

# NĆµuded:
# * Kasutajaliides tuleb luua Tkinteri abil, et pakkuda kasutajasĆµbralikku ja intuitiivset navigeerimist.
# * Rakendus peab tagama andmete jĆ¤rjepidevuse ja turvalisuse, kasutades failipĆµhist salvestusviisi.
# * Unikaalse laenutus-ID genereerimine peab tagama, et iga laenutus on selgelt identifitseeritav.
# * Rakendus peab vĆµimaldama raamatute ja lugejate andmete lihtsat sisestamist, muutmist ja kustutamist, samuti laenutusprotsessi haldamist.
# * Failid peavad olema kĆ¤ttesaadavad Githubis




from ctypes import LibraryLoader
import tkinter as tk
import csv
from tkinter import messagebox
import uuid
from tkinter import Entry

import tkinter as tk
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

    def view_books(self):
        for book in self.books:
            print(book)

    def view_readers(self):
        for reader in self.readers:
            print(reader)

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

    def loan_book(self, book_id, reader_id):
        loan_id = uuid.uuid4()
        self.loans.append({'id': loan_id, 'book_id': book_id, 'reader_id': reader_id})
        return loan_id

    def return_book(self, loan_id):
        self.loans = [loan for loan in self.loans if loan['id'] != loan_id]

    def save_data(self):
        with open('books.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['id', 'title', 'author', 'year'])
            writer.writeheader()
            writer.writerows(self.books)

        with open('readers.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['id', 'name', 'contact'])
            writer.writeheader()
            writer.writerows(self.readers)

        with open('loans.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['id', 'book_id', 'reader_id'])
            writer.writeheader()
            writer.writerows(self.loans)

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

        try:
            with open('loans.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                self.loans = list(reader)
        except FileNotFoundError:
            pass

class Library:
    def __init__(self):
        self.books = []
        self.readers = []

    def add_book(self, title, author, year):
        self.books.append({"Pealkiri": title, "Autor": author, "Aasta": year})

    def add_reader(self, name, contact):
        self.readers.append({"Nimi": name, "Kontakt": contact})

    def modify_book(self, title):
        new_title = tk.simpledialog.askstring("Raamatu muutmine", "Sisestage uus pealkiri:")
        if new_title:
            for book in self.books:
                if book["Pealkiri"] == title:
                    book["Pealkiri"] = new_title
                    messagebox.showinfo("Raamatu muutmine", "Raamat on edukalt muudetud.")
                    return

    def delete_book(self, title):
        for book in self.books:
            if book["Pealkiri"] == title:
                self.books.remove(book)
                messagebox.showinfo("Raamatu kustutamine", "Raamat on edukalt kustutatud.")
                return

    def modify_reader(self, name):
        new_name = tk.simpledialog.askstring("Lugeja muutmine", "Sisestage uus nimi:")
        if new_name:
            for reader in self.readers:
                if reader["Nimi"] == name:
                    reader["Nimi"] = new_name
                    messagebox.showinfo("Lugeja muutmine", "Lugeja on edukalt muudetud.")
                    return

    def delete_reader(self, name):
        for reader in self.readers:
            if reader["Nimi"] == name:
                self.readers.remove(reader)
                messagebox.showinfo("Lugeja kustutamine", "Lugeja on edukalt kustutatud.")
                return

    def save_data(self):
        with open('books.csv', 'w', newline='') as csvfile:
            fieldnames = ['Pealkiri', 'Autor', 'Aasta']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for book in self.books:
                writer.writerow(book)

        with open('readers.csv', 'w', newline='') as csvfile:
            fieldnames = ['Nimi', 'Kontakt']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for reader in self.readers:
                writer.writerow(reader)

    def load_data(self):
        try:
            with open('books.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    self.books.append(row)
        except FileNotFoundError:
            pass

        try:
            with open('readers.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    self.readers.append(row)
        except FileNotFoundError:
            pass


library = Library()

root = tk.Tk()

# Create book entry fields
tk.Label(root, text="Book Title").grid(row=0)
tk.Label(root, text="Author").grid(row=1)
tk.Label(root, text="Publication Year").grid(row=2)

title_entry = tk.Entry(root)
author_entry = tk.Entry(root)
year_entry = tk.Entry(root)

title_entry.grid(row=0, column=1)
author_entry.grid(row=1, column=1)
year_entry.grid(row=2, column=1)

# Create reader entry fields
tk.Label(root, text="Reader Name").grid(row=3)
tk.Label(root, text="Contact Info").grid(row=4)

name_entry = tk.Entry(root)
contact_entry = tk.Entry(root)

name_entry.grid(row=3, column=1)
contact_entry.grid(row=4, column=1)

# Create buttons to add book and reader
tk.Button(root, text='Add Book', command=lambda: library.add_book(title_entry.get(), author_entry.get(), year_entry.get())).grid(row=5, column=0, sticky=tk.W, pady=4)
tk.Button(root, text='Add Reader', command=lambda: library.add_reader(name_entry.get(), contact_entry.get())).grid(row=5, column=1, sticky=tk.W, pady=4)

# Create listboxes to display books and readers
books_listbox = tk.Listbox(root)
readers_listbox = tk.Listbox(root)

books_listbox.grid(row=6, column=0)
readers_listbox.grid(row=6, column=1)

# Create buttons to modify and delete books and readers
tk.Button(root, text='Modify Book', command=lambda: library.modify_book(books_listbox.get(tk.ACTIVE))).grid(row=7, column=0, sticky=tk.W, pady=4)
tk.Button(root, text='Delete Book', command=lambda: library.delete_book(books_listbox.get(tk.ACTIVE))).grid(row=7, column=1, sticky=tk.W, pady=4)
tk.Button(root, text='Modify Reader', command=lambda: library.modify_reader(readers_listbox.get(tk.ACTIVE))).grid(row=8, column=0, sticky=tk.W, pady=4)
tk.Button(root, text='Delete Reader', command=lambda: library.delete_reader(readers_listbox.get(tk.ACTIVE))).grid(row=8, column=1, sticky=tk.W, pady=4)

root.mainloop()

