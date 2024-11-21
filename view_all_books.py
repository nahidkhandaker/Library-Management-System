def view_all_books(all_books):
    if all_books != []:
        for book in all_books:
            print(f"ID: {book['id']} | Title: {book['title']} | Author: {book['author']} | Year: {book['year']} | ISBN: {book['isbn']} | Price: {book['price']} | Quantity: {book['quantity']}")
    else:
        print("No books found in the library.")

