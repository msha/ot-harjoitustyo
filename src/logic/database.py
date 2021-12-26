import sqlite3
from sqlite3 import Error

class Database:
    def __init__(self):
        try:
            self.current_db = sqlite3.connect('data.db')
        except Error as err:
            print(err)
        self._cursor = self.current_db.cursor()
        try:
            self.create_table_files()
        except Error as err:
            print(err)

    def create_table_files(self):
        self._cursor.execute("""CREATE TABLE files 
                            (id INTEGER PRIMARY KEY, path TEXT, modified DATETIME DEFAULT CURRENT_TIMESTAMP)""")
        self.current_db.commit()

    def insert_record(self,filename):
        print("kirjoitan")
        self._cursor.execute(f"""INSERT INTO files(path)
                                VALUES('{filename}')""")
        self.current_db.commit()
    
    def get_recent(self):
        self._cursor.execute("""SELECT path 
                                FROM files 
                                ORDER BY modified DESC
                                LIMIT 5""")

        return self._cursor.fetchall()

    
