import os
from logic.database import Database

class Fileops:
    '''Handles filemanipulations'''

    def __init__(self):
        self.working_file = 'untitled'
        self.db = Database()

    def savefile(self,name,content):
        with open(name, "w",encoding="utf-8") as file:
            self.working_file = os.path.basename(name)
            file.write(content)
            self.db.insert_record(name)

    def openfile(self,name):
        with open(name, "r",encoding="utf-8") as file:
            self.working_file = os.path.basename(name)
            return file.read()


    def filename(self):
        return self.working_file
