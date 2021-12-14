class Code:
    '''Handles behind the scenes code manipulations so that actions are interpreted as they should'''
    def __init__(self,code = "<a>testi</a>"):
        self._code = code
        self.currenttag = ''
        self.pointer = len(code)
        self.pointer2 = len(code)

    def read_code(self):
        return self._code

    def save_code(self,new_code):
        self._code = new_code

    def insert_code(self,new_code):
        self._code = self._code[:self.pointer]+new_code+self._code[self.pointer:]
        self.pointer += len(new_code)

    def delete_code(self):
        self._code = self._code[:self.pointer-1]+self._code[self.pointer:]
        self.pointer -= 1
    
    def special_command(self,event):
        '''Read special characters and convert them into an appropriate action'''
        def backspace():
            self.delete_code()
        
        def enter():
            self.insert_code('<br>')
        
        def space():
            self.insert_code(' ')
        
        def move_left():
            self.pointer -=2
        def move_right():
            self.pointer += 2

        command={
            'BackSpace': backspace,
            'Return': enter,
            'space': space,
            'Left': move_left,
            'Right': move_right
        }
        if event in command:
            command.get(event)()
