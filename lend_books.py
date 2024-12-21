from save_all_books import save_all_books
from save_lend_records import save_lend_records
from datetime import datetime, timedelta

def lend_books(all_books, lend_records):
    if not all_books:
        print("No books available in the library.")
        return all_books, lend_records
    
    book_title = input("Enter book title to lend: ")
    book_found = False

    for book in all_books:
        if book["title"].lower() == book_title.lower():
            book_found = True

            try:
                curent_quantity = int(book["quantity"])
                if curent_quantity > 0:
                    borrower_name = input("Enter borrower's name: ").strip()
                    if not borrower_name:
                        print("Borrower's name cannot be empty.")
                        return all_books, lend_records
                    
                    phone_number = input("Enter borrowe's phone number: ").strip()
                    if not phone_number:
                        print("Phone number cannot be empty.")
                        return all_books, lend_records

                    # create landind record
                    borrow_date = datetime.now()
                    due_date = borrow_date + timedelta(days=14) # 2-week landing period

                    lend_record = {
                        "borrower_name": borrower_name,
                        "phone_number": phone_number,
                        "book_title": book_title,
                        "borrow_date": borrow_date.strftime('%d-%m-%Y %H:%M:%S'),
                        "due_date": due_date.strftime('%d-%m-%Y %H:%M:%S'),
                        "book_id": book["id"] # adding book ID for better tracking
                    }

                    # update book quantity
                    book["quantity"] = str(int(book["quantity"]) -1)

                    # add lending record
                    lend_records.append(lend_record)

                    # save updates
                    save_all_books(all_books)
                    save_lend_records(lend_records)

                    print(f"Book lent successfully! Due date: {due_date.strftime('%d-%m-%Y')}")
                    print(f"Remaining copies: {book['quantity']}")
                else:
                    print("Book not available. Please try another book.")
            except ValueError as e:
                print(f"Error processing book quantity: {e}")
            break

    if not book_found:
        print("Book not found in library.")

    return all_books, lend_records