import csv

# Define fieldnames
fieldnames = ['id', 'title', 'author', 'year']

# Sample data for books
books_data = [
    {'id': 1, 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'year': 1960},
    {'id': 2, 'title': '1984', 'author': 'George Orwell', 'year': 1949},
    {'id': 3, 'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'year': 1925},
    {'id': 4, 'title': 'Pride and Prejudice', 'author': 'Jane Austen', 'year': 1813},
    {'id': 5, 'title': 'The Catcher in the Rye', 'author': 'J.D. Salinger', 'year': 1951},
    {'id': 6, 'title': 'To the Lighthouse', 'author': 'Virginia Woolf', 'year': 1927},
    {'id': 7, 'title': 'Moby-Dick', 'author': 'Herman Melville', 'year': 1851},
    {'id': 8, 'title': 'Brave New World', 'author': 'Aldous Huxley', 'year': 1932},
    {'id': 9, 'title': 'The Hobbit', 'author': 'J.R.R. Tolkien', 'year': 1937},
    {'id': 10, 'title': 'Frankenstein', 'author': 'Mary Shelley', 'year': 1818},
    {'id': 11, 'title': 'The Lord of the Rings', 'author': 'J.R.R. Tolkien', 'year': 1954},
    {'id': 12, 'title': 'Jane Eyre', 'author': 'Charlotte Brontë', 'year': 1847},
    {'id': 13, 'title': 'Animal Farm', 'author': 'George Orwell', 'year': 1945},
    {'id': 14, 'title': 'The Odyssey', 'author': 'Homer', 'year': -800},
    {'id': 15, 'title': 'The Picture of Dorian Gray', 'author': 'Oscar Wilde', 'year': 1890},
    {'id': 16, 'title': 'The Brothers Karamazov', 'author': 'Fyodor Dostoevsky', 'year': 1880},
    {'id': 17, 'title': 'Wuthering Heights', 'author': 'Emily Brontë', 'year': 1847},
    {'id': 18, 'title': 'The Grapes of Wrath', 'author': 'John Steinbeck', 'year': 1939},
    {'id': 19, 'title': 'Crime and Punishment', 'author': 'Fyodor Dostoevsky', 'year': 1866},
    {'id': 20, 'title': 'Anna Karenina', 'author': 'Leo Tolstoy', 'year': 1877},
    {'id': 21, 'title': 'One Hundred Years of Solitude', 'author': 'Gabriel García Márquez', 'year': 1967},
    {'id': 22, 'title': 'The Divine Comedy', 'author': 'Dante Alighieri', 'year': 1320},
    {'id': 23, 'title': 'Gone with the Wind', 'author': 'Margaret Mitchell', 'year': 1936},
    {'id': 24, 'title': 'The Canterbury Tales', 'author': 'Geoffrey Chaucer', 'year': 1400},
    {'id': 25, 'title': 'Les Misérables', 'author': 'Victor Hugo', 'year': 1862},
    {'id': 26, 'title': 'Great Expectations', 'author': 'Charles Dickens', 'year': 1861},
    {'id': 27, 'title': 'The Stranger', 'author': 'Albert Camus', 'year': 1942},
    {'id': 28, 'title': 'The Bell Jar', 'author': 'Sylvia Plath', 'year': 1963},
    {'id': 29, 'title': 'Slaughterhouse-Five', 'author': 'Kurt Vonnegut', 'year': 1969},
    {'id': 30, 'title': 'The Sun Also Rises', 'author': 'Ernest Hemingway', 'year': 1926},
    {'id': 31, 'title': 'Middlemarch', 'author': 'George Eliot', 'year': 1871},
    {'id': 32, 'title': 'A Tale of Two Cities', 'author': 'Charles Dickens', 'year': 1859},
    {'id': 33, 'title': 'The Road', 'author': 'Cormac McCarthy', 'year': 2006},
    {'id': 34, 'title': 'The Count of Monte Cristo', 'author': 'Alexandre Dumas', 'year': 1844},
    {'id': 35, 'title': 'The Iliad', 'author': 'Homer', 'year': -800},
    {'id': 36, 'title': 'The Scarlet Letter', 'author': 'Nathaniel Hawthorne', 'year': 1850},
    {'id': 37, 'title': 'Beloved', 'author': 'Toni Morrison', 'year': 1987},
    {'id': 38, 'title': 'The Handmaid\'s Tale', 'author': 'Margaret Atwood', 'year': 1985},
    {'id': 39, 'title': 'The Adventures of Huckleberry Finn', 'author': 'Mark Twain', 'year': 1884},
    {'id': 40, 'title': 'Fahrenheit 451', 'author': 'Ray Bradbury', 'year': 1953},
]

# Write data to CSV file
with open('books.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    for book in books_data:
        writer.writerow(book)