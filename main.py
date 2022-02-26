import sqlite3
import visitors as vs
import books as bk
import booklist as bl
import random

visitors = vs.selectTableVisitors1()

for visitor in visitors:
    books = bl.selectBooks(visitor)
    print(books[0][0], books[0][1], books[0][2], end=": ")
    for book in books:
        print("Книга:",book[3], "Автор:",book[4], end=", ")
    print()














