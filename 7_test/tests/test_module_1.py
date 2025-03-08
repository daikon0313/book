from src.module_1 import add_numbers

def test_add_numbers_1():
    assert add_numbers(1,2) == 3

def test_add_numbers_2():
    assert add_numbers(-1,-2) == -3

from src.module_1 import all_books

import sqlite3
def test_all_books():
    con = sqlite3.connect("local_database.db")
    books = all_books(con)
    assert books == []
    con.close