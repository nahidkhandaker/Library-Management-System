def view_lend_records(lend_records):
    if lend_records:
        print("\nCurrent Lending Records: ")
        print("-" * 80)

        for record in lend_records:
            # First try 'borrewer_name', then 'borrower_name', then default to 'N/A'
            borrower_name = record.get('borrewer_name', record.get('borrower_name', 'N/A'))
            phone = record.get('phone_number', 'N/A')
            book = record.get('book_title', 'N/A')
            due_date = record.get('due_date', 'N/A')
            
            print(f"Borrower: {borrower_name} | "
                  f"Phone: {phone} | "
                  f"Book: {book} | "
                  f"Due Date: {due_date}")
            
        print("-" * 80)

    else:
        print("\nNo books are currently lent out.")

    
    