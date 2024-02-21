

import tkinter as tk
from tkinter import messagebox
import csv

class LibrarySystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Raamatukogu laenutussüsteem")
        
        self.books = []
        self.readers = []
        self.load_data()
        
        self.menu_frame = tk.Frame(self.root)
        self.menu_frame.pack(padx=20, pady=20)
        
        self.title_label = tk.Label(self.menu_frame, text="Raamatukogu Laenutussüsteem", font=("Helvetica", 18))
        self.title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        
        self.add_book_button = tk.Button(self.menu_frame, text="Lisa raamat", command=self.add_book)
        self.add_book_button.grid(row=1, column=0, padx=10, pady=10)
        
        self.add_reader_button = tk.Button(self.menu_frame, text="Lisa lugeja", command=self.add_reader)
        self.add_reader_button.grid(row=1, column=1, padx=10, pady=10)
        
        self.show_books_button = tk.Button(self.menu_frame, text="Näita raamatuid", command=self.show_books)
        self.show_books_button.grid(row=2, column=0, padx=10, pady=10)
        
        self.show_readers_button = tk.Button(self.menu_frame, text="Näita lugejaid", command=self.show_readers)
        self.show_readers_button.grid(row=2, column=1, padx=10, pady=10)
        
        self.save_button = tk.Button(self.menu_frame, text="Salvesta", command=self.save_data)
        self.save_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        
    def add_book(self):
        title = tk.simpledialog.askstring("Raamatu lisamine", "Sisestage raamatu pealkiri:")
        author = tk.simpledialog.askstring("Raamatu lisamine", "Sisestage raamatu autor:")
        year = tk.simpledialog.askinteger("Raamatu lisamine", "Sisestage raamatu väljaandeaasta:")
        if title and author and year:
            self.books.append({"Pealkiri": title, "Autor": author, "Aasta": year})
            messagebox.showinfo("Raamatu lisamine", "Raamat on edukalt lisatud.")
    
    def add_reader(self):
        name = tk.simpledialog.askstring("Lugeja lisamine", "Sisestage lugeja nimi:")
        contact = tk.simpledialog.askstring("Lugeja lisamine", "Sisestage lugeja kontaktandmed:")
        if name and contact:
            self.readers.append({"Nimi": name, "Kontakt": contact})
            messagebox.showinfo("Lugeja lisamine", "Lugeja on edukalt lisatud.")
    
    def show_books(self):
        if self.books:
            messagebox.showinfo("Raamatud", "\n".join([f"{book['Pealkiri']} - {book['Autor']} ({book['Aasta']})" for book in self.books]))
        else:
            messagebox.showinfo("Raamatud", "Raamatute nimekiri on tühi.")
    
    def show_readers(self):
        if self.readers:
            messagebox.showinfo("Lugejad", "\n".join([f"{reader['Nimi']}: {reader['Kontakt']}" for reader in self.readers]))
        else:
            messagebox.showinfo("Lugejad", "Lugejate nimekiri on tühi.")
    
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

if __name__ == "__main__":
    root = tk.Tk()
    app = LibrarySystem(root)
    root.mainloop()
