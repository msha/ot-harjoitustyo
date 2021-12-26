import sqlite3
from sqlite3 import Error

class Database:
    def __init__(self):
        try:
            current_db = sqlite3.connect('data.db')
        except Error as err:
            print(err)

        self._cursor = current_db.cursor()

    def create_table_files(self):
        self._cursor.execute("CREATE TABLE files (id INTEGER PRIMARY KEY, path TEXT)")
