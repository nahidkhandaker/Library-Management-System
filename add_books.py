from save_all_books import save_all_books

def add_books(all_books):
    id = input('Enter an ID: ')
    title = input("Enter Book Title: ")
    author = input("Enter Book Author: ")
    year = int(input("Enter Publishing Year: "))
    isbn = int(input("Enter ISBN Number: "))
    price = int(input("Enter Book Price: "))
    quantity = int(input("Enter Quantity: "))

    book = {
        "id": id,
        "title": title,
        "author": author,
        "year": year,
        "isbn": isbn,
        "price": price,
        "quantity": quantity
    }

    all_books.append(book)
    save_all_books(all_books)

    print ('Books added successfully. ')
    
    return all_books

