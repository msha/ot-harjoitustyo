import os
from logic.database import Database

class Fileops:
    '''Handles filemanipulations'''

    def __init__(self):
        self.working_file = 'untitled'

    def savefile(self,name,content):
        with open(name, "w",encoding="utf-8") as file:
            file.write(content)

    def openfile(self,name):
        with open(name, "r",encoding="utf-8") as file:
            self.working_file = os.path.basename(name)
            return file.read()

    def save_as_file(self,name,content):
        with open(name, "w",encoding="utf-8") as file:
            file.write(content)

    def filename(self):
        return self.working_file
