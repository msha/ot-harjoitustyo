from tkinter import Menu,Frame,PhotoImage,Button,Toplevel,Text,Tk,RIGHT,BOTTOM,YES
from tkhtmlview import HTMLLabel
from codeops import Code
from fileops import Fileops

class Gui:

    def __init__(self):
        self.root = Tk()
        self.code = Code()
        self.htmlview = HTMLLabel(self.root, html=self.code)
        self.htmlview.configure(bg='white')


    def menu(self):


        menubar = Menu(self.root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command='')
        filemenu.add_command(label="Save", command= self.save)

        filemenu.add_separator()

        filemenu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        self.root.config(menu=menubar)

    def save(self):
        Fileops.savefile(self,"testi.html",self.code.read_code())

    def tools(self):
        button_frame = Frame(self.root)
        button_frame.pack()
        bg_icon = PhotoImage(file='./img/background.png')

        self.button_background = Button(
            button_frame,
            text ="Background",
            command = '')
        self.button_background.pack(side = RIGHT)
        add_text = Button(
            button_frame,
            text ="Code",
            command = self.create_window)
        add_text.pack(side = RIGHT,expand=YES)

    def create_window(self):
        window = Toplevel(self.root)
        window.geometry("450x250")
        tekstin_syotto = Text(
            window,
            height=12,
            width=40
        )
        tekstin_syotto.insert('end',self.code.read_code())
        tekstin_syotto.pack(expand=True)

        def close():
            self.code.save_code(tekstin_syotto.get(1.0,'end'))
            window.destroy()

        save = Button(
            window,
            text ="Save",
            command = close)
        save.pack(side = BOTTOM)


    def html_area(self):
        self.htmlview.set_html(self.code.read_code(),True)
        self.htmlview.after(1000,self.html_area)

    def start(self):
        self.menu()
        self.tools()
        self.htmlview.pack(fill="both", expand=True)
        self.html_area()
        self.root.mainloop()
