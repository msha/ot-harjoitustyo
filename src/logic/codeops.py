class Code:
    '''Handles behind the scenes code manipulations
    so that actions are interpreted as they should'''
    def __init__(self,code = "<a>testi</a>"):
        self._code = code
        self.currenttag = ''
        self.htmlview_cursor_location = 1.1

    def read_code(self):
        return self._code

    def save_code(self,new_code):
        self._code = '<a>'+new_code+'</a>'

    def insert_code(self,new_code):
        self._code += new_code

    # def delete_code(self):
    #     self._code = self._code[:self.pointer-1]+self._code[self.pointer:]
    #     # self.pointer -= 1

    def set_cursor(self,value):
        self.htmlview_cursor_location = value
        print(self.htmlview_cursor_location)

    def get_cursor(self):
        return self.htmlview_cursor_location

    def special_command(self,event):
        '''Read special characters and convert them into an appropriate action'''
        def backspace():
            self.delete_code()

        def enter():
            self.insert_code('<br>')

        def space():
            self.insert_code(' ')

        command={
            'BackSpace': backspace,
            'Return': enter,
            'space': space
        }
        if event in command:
            command.get(event)()
