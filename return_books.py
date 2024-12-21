from save_all_books import save_all_books
from save_lend_records import save_lend_records

def return_books(all_books, lend_records):
    borrower_name = input("Enter borrower's name: ")
    book_title = input("Enter book title being returned: ")

    # find and remove landing record
    record_found = False
    for record in lend_records[:]: # create a copy of the list to iterate
        if (record.get("borrower_name", "").lower() == borrower_name.lower() and 
            record.get("book_title", "").lower() == book_title.lower()):
            lend_records.remove(record)
            record_found = True

            # update book quantity
            for book in all_books:
                if book.get("title", "").lower() == book_title.lower():
                    book["quantity"] = str(int(book["quantity"]) + 1)
                    break
            
            # save updates 
            save_all_books(all_books)
            save_lend_records(lend_records)

            print("Book returned successfully.")
            break

    if not record_found:
        print("No matching lending record found.")

    return all_books, lend_records