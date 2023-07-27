'''
storing and retrieving books from a list 

'''

books = []

#add new, retrieve...

def add_book(name, author):
    books.append({'name': name, 'author': author, 'read': False})

def get_all_books():
    return books

def mark_book_as_read(name):
    for book in book:
        if book['name'] == name:
            book['read'] = True 

def delete_book(name):
    # for book in books:
    #     if book['name'] == name:
    #         books.remove(book)
    global books #makes it a global variable 
    #add each book to new list if name isn't equal 
    books = [book for book in books if book['name'] != name]


