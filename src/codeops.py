class Code:

    def __init__(self,code = "<a>testi</a>"):
        self.code = code
        self.pointer = len(code)

    def read_code(self):
        return self.code

    def save_code(self,new_code):
        self.code = new_code

    def insert_code(self,new_code):
        if new_code == '\x08':
            self.delete_code()
        elif new_code == '\r':
            self.code += '<br>'
        else:
            print("liikuin "+str(self.pointer))
            self.code = self.code[:self.pointer]+new_code+self.code[self.pointer:]
            self.pointer += 1

    def delete_code(self):
        self.code = self.code[:self.pointer-1]+self.code[self.pointer:]
        self.pointer -= 1
    
    def move_pointer(self,symbol):
        def move_left():
            self.pointer -=2
        def move_right():
            self.pointer += 1

        command={
            'Left': move_left(),
            'Right': move_right()
        }

        command.get(symbol)