from save_all_books import save_all_books

def delete_books(all_books):
    search_book = input("Enter book title to delete: ")
    
    for book in all_books:
        if book["title"] == search_book: 
            all_books.remove(book)
            
            print("Book deleted successfully")
            break  # Exit the loop after deleting the book

    if not search_book:
        print("Book with the given title not found.")

    # Save the updated book list back to the CSV file
    save_all_books(all_books)
    return all_books