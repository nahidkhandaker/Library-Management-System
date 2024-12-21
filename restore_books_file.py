import json

def restore_all_books(all_books):
    with open("books.json", "r") as fp:
        all_books = json.load(fp)
    return all_books
