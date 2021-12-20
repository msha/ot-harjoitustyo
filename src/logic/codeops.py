from tkinter import font
import re

class Code:
    '''Handles behind the scenes code manipulations
    so that actions are interpreted as they should'''
    def __init__(self,code = '''<h1>otsikko</h1></br><a>testi</a></br><p>asdf</p><h2>alaotsikko</h2><a>viimeinen</a>'''):
        self._code = code
        self.currenttag = ''
        self.htmlview_cursor_location = 1.1


    def read_code(self):
        return self._code

    def save_code(self,new_code):
        self._code = ''
        for (key, value, index) in new_code:
            print(key+'  : '+value+' : '+index)
            if key == "text" and (value=='\n' or value =='\r' or value =='\r\n'):
                self._code += '<br>'
            elif key == "text" and len(value) > 0 and value is not ' ':
                self._code += '<a>'+value+'</a>'

    def insert_code(self,new_code):
        self._code += new_code

    def codelen(self):
        regex = re.compile(r'<.*?>')
        return len(regex.sub('',self._code))+self._code.count('/')

    # def delete_code(self):
    #     self._code = self._code[:self.pointer-1]+self._code[self.pointer:]
    #     # self.pointer -= 1

    def set_cursor(self,value):
        self.htmlview_cursor_location = value

    def get_cursor(self):
        return self.htmlview_cursor_location

    def special_command(self,event):
        '''Read special characters and convert them into an appropriate action'''
        def backspace():
            pass

        def enter():
            self.insert_code('</br>')

        def space():
            self.insert_code(' ')

        command={
            'BackSpace': backspace,
            'Return': enter,
            'space': space
        }
        if event in command:
            command.get(event)()
