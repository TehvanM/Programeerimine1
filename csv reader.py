import csv

# Define fieldnames for readers
reader_fieldnames = ['id', 'name', 'contact']

# Sample data for readers
readers_data = [
    {'id': 1, 'name': 'John Doe', 'contact': 'john@example.com'},
    {'id': 2, 'name': 'Jane Smith', 'contact': 'jane@example.com'},
    {'id': 3, 'name': 'David Johnson', 'contact': 'david@example.com'},
    {'id': 4, 'name': 'Emily Brown', 'contact': 'emily@example.com'},
    {'id': 5, 'name': 'Michael Wilson', 'contact': 'michael@example.com'},
    {'id': 6, 'name': 'Emma Jones', 'contact': 'emma@example.com'},
    {'id': 7, 'name': 'Daniel Taylor', 'contact': 'daniel@example.com'},
    {'id': 8, 'name': 'Olivia Martinez', 'contact': 'olivia@example.com'},
    {'id': 9, 'name': 'William Anderson', 'contact': 'william@example.com'},
    {'id': 10, 'name': 'Sophia Thomas', 'contact': 'sophia@example.com'},
    {'id': 11, 'name': 'Joseph White', 'contact': 'joseph@example.com'},
    {'id': 12, 'name': 'Isabella Jackson', 'contact': 'isabella@example.com'},
    {'id': 13, 'name': 'James Harris', 'contact': 'james@example.com'},
    {'id': 14, 'name': 'Charlotte Carter', 'contact': 'charlotte@example.com'},
    {'id': 15, 'name': 'Benjamin Nelson', 'contact': 'benjamin@example.com'},
    {'id': 16, 'name': 'Amelia Allen', 'contact': 'amelia@example.com'},
    {'id': 17, 'name': 'Elijah King', 'contact': 'elijah@example.com'},
    {'id': 18, 'name': 'Mia Lewis', 'contact': 'mia@example.com'},
    {'id': 19, 'name': 'Logan Walker', 'contact': 'logan@example.com'},
    {'id': 20, 'name': 'Avery Green', 'contact': 'avery@example.com'},
    {'id': 21, 'name': 'Harper Perez', 'contact': 'harper@example.com'},
    {'id': 22, 'name': 'Jackson Hall', 'contact': 'jackson@example.com'},
    {'id': 23, 'name': 'Lily Young', 'contact': 'lily@example.com'},
    {'id': 24, 'name': 'Aiden Moore', 'contact': 'aiden@example.com'},
    {'id': 25, 'name': 'Ella Clark', 'contact': 'ella@example.com'},
    {'id': 26, 'name': 'Carter Hill', 'contact': 'carter@example.com'},
    {'id': 27, 'name': 'Grace Ward', 'contact': 'grace@example.com'},
    {'id': 28, 'name': 'Lucas Scott', 'contact': 'lucas@example.com'},
    {'id': 29, 'name': 'Aria Flores', 'contact': 'aria@example.com'},
    {'id': 30, 'name': 'Henry Adams', 'contact': 'henry@example.com'},
    {'id': 31, 'name': 'Addison Rivera', 'contact': 'addison@example.com'},
    {'id': 32, 'name': 'Evelyn Price', 'contact': 'evelyn@example.com'},
    {'id': 33, 'name': 'Matthew Cook', 'contact': 'matthew@example.com'},
    {'id': 34, 'name': 'Natalie Cooper', 'contact': 'natalie@example.com'},
    {'id': 35, 'name': 'Dylan Bailey', 'contact': 'dylan@example.com'},
    {'id': 36, 'name': 'Zoey Rogers', 'contact': 'zoey@example.com'},
    {'id': 37, 'name': 'Gabriel Morgan', 'contact': 'gabriel@example.com'},
    {'id': 38, 'name': 'Leah Reed', 'contact': 'leah@example.com'},
    {'id': 39, 'name': 'Christopher Ward', 'contact': 'christopher@example.com'},
    {'id': 40, 'name': 'Sofia Wright', 'contact': 'sofia@example.com'},
]

# Write data to CSV file
with open('readers.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=reader_fieldnames)

    writer.writeheader()
    for reader in readers_data:
        writer.writerow(reader)
