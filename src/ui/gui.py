from tkinter import Menu,Frame,PhotoImage,Button,Toplevel,Text,Tk,filedialog,RIGHT,BOTTOM,YES,font
from tkinter.constants import INSERT, TOP
from tkhtmlview import HTMLLabel,HTMLScrolledText
from logic.codeops import Code
from logic.fileops import Fileops

class Gui:

  def __init__(self):
    self.root = Tk()
    self.root.geometry("1280x720")
    self.root.title("Editor")

    self._code = Code()
    self.htmlview = HTMLScrolledText(self.root, html=self._code)
    self.htmlview.configure(bg='white')


  def menu(self):
    '''Top menu in GUI'''

    menubar = Menu(self.root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command='')
    filemenu.add_command(label="Save", command= self.save)
    filemenu.add_command(label="Save as", command= self.save)

    filemenu.add_separator()

    filemenu.add_command(label="Exit", command=self.root.quit)
    menubar.add_cascade(label="File", menu=filemenu)

    self.root.config(menu=menubar)

  def save(self):
    Fileops.savefile(self,"testi.html",self._code.read_code())

  def tools(self):
    '''Tool area in GUI'''
    button_frame = Frame(self.root)
    button_frame.pack()
    bg_icon = PhotoImage(file='./img/background.png')

    self.button_background = Button(
      button_frame,
      text ="Background",
      command = '')
    self.button_background.pack(side = RIGHT)
    view_code = Button(
      button_frame,
      text ="Code",
      command = self.create_window_code)
    view_code.pack(side = RIGHT,expand=YES)
    text_tools = Button(
      button_frame,
      text ="Text",
      command = self.create_window_code)
    text_tools = Button(
      button_frame,
      text ="Bold",
      command = self.bold_it)
    text_tools.pack(side = RIGHT,expand=YES)
    add_image = Button(
      button_frame,
      text ="Add Image",
      command = self.create_window_image)
    add_image.pack(side = RIGHT,expand=YES)


  def create_window_code(self):
    '''Window for viewing code'''
    window = Toplevel(self.root)
    window.geometry("450x250")
    tekstin_syotto = Text(
      window,
      height=12,
      width=40
    )
    tekstin_syotto.insert('end',self._code.read_code())
    tekstin_syotto.pack(expand=True)

    def close():
      self._code.save_code(tekstin_syotto.get(1.0,'end'))
      window.destroy()

    save = Button(
      window,
      text ="Save",
      command = close)
    save.pack(side = BOTTOM)

  def create_window_image(self):
    ''''Window for adding images'''
    window = Toplevel(self.root)
    window.geometry("450x250")
    filepath = Text(
      window,
      height=1,
      width=40
    )
    def open_file():
      file_path = filedialog.askopenfilename(parent=window,
        filetypes=[("Images","*.jpg *.png *.gif *.webp *.jpeg")],title='Choose a file')
      filepath.insert('end',file_path)

    def close():
      self._code.insert_code('<img src='+filepath.get(1.0,'end')+'></img>')
      window.destroy()
      self.render_html_area()

    browse = Button(
      window,
      text ="Browse images",
      command = open_file)
    save = Button(
      window,
      text ="Save",
      command = close)
    filepath.pack(side=TOP)
    browse.pack(side=TOP,pady=20)
    save.pack(side = BOTTOM)

  def bold_it(self):
    bold_font = font.Font(self.root, self.htmlview.cget("font"))
    bold_font.configure(weight="italic")

    self.htmlview.tag_configure("bold", font=bold_font)
    self.htmlview.tag_add("bold",1.0,'end')

  def render_html_area(self):
    '''Render of the work in progress HTML'''
    self.htmlview.set_html(self._code.read_code(),True)
    self.htmlview.mark_set("insert", self._code.get_cursor())
    print(self.htmlview.get('1.0', 'end'))

  def on_key_press(self,event):
    '''Listing to keyevents and converting them into inputs'''
    self._code.set_cursor(self.htmlview.index(INSERT))
    self._code.save_code(self.htmlview.get(1.0,"end"))
    if event.char == event.keysym:
      pass
    else:
      self._code.special_command(event.keysym)
    self.render_html_area()
    


  def start(self):
    self.menu()
    self.tools()
    self.htmlview.pack(fill="both", expand=True)
    self.render_html_area()
    self.root.bind('<KeyPress>', self.on_key_press)
    self.root.mainloop()
