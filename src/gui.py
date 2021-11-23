from tkinter import *
from tkhtmlview import HTMLLabel

class Gui:

    def __init__(self):
        self.root = Tk()
        self.derp = 0
        self.code = """
        <html>
        <head>
        <style>
            body {
                background-color: white;
            }
        </style>
        </head>
        <body>
        <h1>testi123d4</h1>
        <p> derp derp </p>
        </body>
        </html>
        """

    def menu(self):

        
        menubar = Menu(self.root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command='')
        filemenu.add_command(label="Save", command='')

        filemenu.add_separator()

        filemenu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        self.root.config(menu=menubar)

    def tools(self):
        button_frame = Frame(self.root)
        button_frame.pack()
        bg_icon = PhotoImage(file='./img/background.png')
        
        self.button_background = Button(button_frame, 
            text ="Background", command = self.hello) 
        self.button_background.pack(side = RIGHT)
        add_text = Button(button_frame, 
            text ="Text", command = '') 
        add_text.pack(side = RIGHT,expand=YES)
        
        
    def htmlArea(self,code):
        
        area = HTMLLabel(self.root, html=code)
        area.pack()

    def hello(self):
        print("sadf")

    def start(self):
        self.menu()
        self.tools()
        self.root.mainloop()