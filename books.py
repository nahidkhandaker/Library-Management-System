import add_books 
import view_all_books
import update
import restore_books_file
import delete_books
import lend_books
import restore_lend_records
import return_books
import view_lend_records

all_books = []
lend_records = []


while True:
    print("Welcome to Library Management System")
    print("0. Exit")
    print("1. Add a book")
    print("2. View all books")
    print("3. Update a book")
    print("4. Delete a book")
    print("5. Lend a book")
    print("6. Return a book")
    print("7. View lend records")

    all_books = restore_books_file.restore_all_books(all_books)
    lend_records = restore_lend_records.restore_lend_records(lend_records)

    menu = input("Select any number: ")

    if menu == '0':
        print("Thanks for using Library Management System.")
        break
    elif menu == '1':
        all_books = add_books.add_books(all_books) 
    
    elif menu == '2':
        all_books = view_all_books.view_all_books(all_books)
    
    elif menu == '3':
        if all_books:
            all_books = update.update_book(all_books)
        else:
            print("No books available to update.")
    
    elif menu == "4":
        all_books = delete_books.delete_books(all_books)
    
    elif menu == "5":
        all_books, lend_records = lend_books.lend_books(all_books, lend_records)

    elif menu == "6":
        all_books, lend_records = return_books.return_books(all_books, lend_records)

    elif menu == "7":
        view_lend_records.view_lend_records(lend_records)
        
    else:
        print("Invalid option. Please select a valid option.")


