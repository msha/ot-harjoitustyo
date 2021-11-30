class Code:

    def __init__(self,code = "<a>testi</a>"):
        self.code = code

    def read_code(self):
        return self.code

    def save_code(self,new_code):
        self.code = new_code
