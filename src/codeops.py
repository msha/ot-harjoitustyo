class Code:

    def __init__(self,code = "<a>testi</a>"):
        self.code = code

    def read_code(self):
        return self.code

    def save_code(self,new_code):
        self.code = new_code

    def insert_code(self,new_code):
        if new_code == '\x08':
            self.code = self.code[:-1]
        elif new_code == '\r':
            self.code += '<br>'
        else:
            self.code += new_code
