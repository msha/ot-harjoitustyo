import os
from logic.database import Database

class Fileops:
    '''Handles filemanipulations'''

    def __init__(self):
        self.working_file = 'untitled'
        self.working_file_path = ''
        self._database = Database()

    def savefile(self,name,content):
        '''save file and insert filelocation to database'''
        with open(name, "w",encoding="utf-8") as file:
            self.working_file = os.path.basename(name)
            self.working_file_path = name
            file.write(content)
            self._database.insert_record(name)

    def openfile(self,name):
        '''returns content of a local file as a string'''
        with open(name, "r",encoding="utf-8") as file:
            self.working_file = os.path.basename(name)
            self.working_file_path = name
            return file.read()


    def filename(self):
        '''return filename of a currently open file'''
        return self.working_file
