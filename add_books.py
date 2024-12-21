from save_all_books import save_all_books
import random
from datetime import datetime

def add_books(all_books):
    id = input('Enter an ID: ')
    title = input("Enter Book Title: ")
    author = input("Enter Book Author: ")

    while True:
        try:
            year = int(input("Enter Publishing Year: "))
            if year < 0:
                print("Year cannot be negative.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid year.")

    # isbn = int(input("Enter ISBN Number: "))
    
    while True:
        try:
            price = int(input("Enter Book Price: "))
            if price < 0:
                print("Price cannot be negative. Please enter a positive value.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    while True:
        try:
            quantity = int(input("Enter Quantity: "))
            if quantity < 0:
                print("Quantity cannot be negative. Please enter a positive value.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer number.")


    isbn = random.randint(10000, 99999) # auto generated isbn number between 10000 to 99999
    bookAddedAt = datetime.now().strftime("%d-%m-%Y %H:%M:%S")



    book = {
        "id": id,
        "title": title,
        "author": author,
        "year": year,
        "isbn": isbn,
        "price": price,
        "quantity": quantity,
        "bookAddedAt": bookAddedAt
    }

    all_books.append(book)
    save_all_books(all_books)

    print ('Books added successfully. ')
    
    return all_books

