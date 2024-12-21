# # update books which is stored in all_books

# from save_all_books import save_all_books
# def update_book(all_books):
#     book_id = input("Enter the book id you want to update: ")
    
#     for book in all_books:
#         if book["id"] == book_id: 
#             book["title"] = input("Enter the new title: ")
#             book["author"] = input("Enter the new author: ")
#             book["price"] = input("Enter the new price: ")
            
#             print("Book updated successfully")



# from save_all_books import save_all_books

# def update_book(all_books):
#     book_id = input("Enter the book id you want to update: ")
#     book_found = False
    
#     for book in all_books:
#         if book["id"] == book_id: 
#             book_found = True
#             book["title"] = input("Enter the new title: ")
#             book["author"] = input("Enter the new author: ")
#             book["price"] = input("Enter the new price: ")
#             book["year"] = input("Enter the new year: ")
#             book["isbn"] = input("Enter the new ISBN: ")
#             book["quantity"] = input("Enter the new quantity: ")

#             print("Book updated successfully")
#             break  # Exit the loop after updating the book

#     if not book_found:
#         print("Book with the given ID not found.")

#     # Save the updated book list back to the CSV file
#     save_all_books(all_books)


from save_all_books import save_all_books
from datetime import datetime

def update_book(all_books):
    search_book = input("Enter book title to update: ")
    
    for book in all_books:
        if book["title"] == search_book: 
            book["title"] = input("Enter the new title: ")
            book["author"] = input("Enter the new author: ")
            book["price"] = input("Enter the new price: ")
            book["year"] = input("Enter the new year: ")
            book["quantity"] = input("Enter the new quantity: ")
            book["book_last_updated_at"] = book_last_updated_at = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

            print("Book updated successfully")
            break  # Exit the loop after updating the book

    if not search_book:
        print("Book with the given title not found.")

    # Save the updated book list back to the CSV file
    save_all_books(all_books)
    return all_books