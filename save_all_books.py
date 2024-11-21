def save_all_books(all_books):
    with open('books.csv','w') as fp:
        for book in all_books:
            line = f"{book['id']}, {book['title']}, {book['author']}, {book['year']}, {book['isbn']}, {book['price']}, {book['quantity']}"
            fp.write(line + '\n')


            