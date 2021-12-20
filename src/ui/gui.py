from tkinter import * #Menu,Frame,PhotoImage,Button,Toplevel,Text,Tk,filedialog,RIGHT,BOTTOM,YES,font,Label
from tkinter.constants import INSERT, TOP
from tkinter import scrolledtext,font,filedialog
from tkhtmlview import HTMLLabel,HTMLScrolledText
from logic.codeops import Code
from logic.fileops import Fileops

class Gui:

  def __init__(self):
    self.root = Tk()
    self.root.geometry("1280x720")
    self.root.title("Editor")

    self._code = Code()
    self.htmlview = scrolledtext.ScrolledText(self.root)
    self.htmlview.configure(bg='white',undo=True)

    self.text_insert_position = self.htmlview.index('insert')
    self.text_current_position = self.htmlview.index('current')
    
    self.debugview = Text(
      self.root,
      height=12,
      width=40
    )

    self.codeview = Text(
      self.root,
      height=12,
      width=40
    )

    self.status = Label(self.root, text = 'adsf',anchor=E) 


  def menu(self):
    '''Top menu in GUI'''

    menubar = Menu(self.root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command='', accelerator="(Ctrl+N)")
    filemenu.add_command(label="Save", command= self.save, accelerator="(Ctrl+S)")
    filemenu.add_command(label="Save as", command= self.save, accelerator="(Ctrl+Shift+S)")

    filemenu.add_separator()

    filemenu.add_command(label="Exit", command=lambda:self.root.quit, accelerator="(Ctrl+Q)")
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
      text ="H1",
      command = self.make_h1_tag)
    redo_button = Button(
      button_frame,
      text ="Redo",
      command = self.htmlview.edit_redo)
    redo_button.pack(side=LEFT,expand=YES)
    undo_button = Button(
      button_frame,
      text ="Undo",
      command = self.htmlview.edit_undo)
    undo_button.pack(side=LEFT)
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

    def close_window():
      self._code.insert_code('<img src='+filepath.get(1.0,'end')+'></img>')
      
      global img 
      img = []
      img.append(PhotoImage(file=filepath.get(1.0,'end-1c')))
      
      self.htmlview.image_create('insert',image=img[len(img)-1])
      window.destroy()
      self.render_html_area()

    browse = Button(
      window,
      text ="Browse images",
      command = open_file)
    save = Button(
      window,
      text ="Save",
      command = close_window)
    filepath.pack(side=TOP)
    browse.pack(side=TOP,pady=20)
    save.pack(side = BOTTOM)
  

  def make_h1_tag(self):
    h1_font = font.Font(size=36)
    self.htmlview.tag_configure("h1", font=h1_font)
    tags = self.htmlview.tag_names('sel.first')
    if "h1" in tags:
      self.htmlview.tag_remove("h1",'sel.first','sel.last')
    else:
      self.htmlview.tag_add("h1",'sel.first','sel.last')

  def render_html_area(self):
    '''Render of the work in progress HTML'''

    self.debugview.delete(1.0,'end')
    self.debugview.insert('end',self.htmlview.dump(1.0,'end'))

    self.codeview.delete(1.0,'end')
    self.codeview.insert('end',self._code.read_code())

    
    
    self.status.config(text="cursor:"+str(self._code.get_cursor())+' , code:'+str(len(self._code.read_code()))+' , stripcode:'+str(self._code.codelen())+ ', html len:'+str(len(self.htmlview.get(1.0,'end-1c'))))
  

  def on_key_press(self,event):
    '''Listing to keyevents and converting them into inputs'''
    
    #print(event.keysym)
    if event.keysym == 'Return':
      
      self.htmlview.insert('insert','\n')
    
    #save and move insert mark to the end of document temporarily to make parsing easier 
    self.text_insert_position = self.htmlview.index('insert')
    self.htmlview.mark_set('insert','end+1c')
    self.htmlview.mark_set('current','end+1c')
    self.htmlview.mark_unset('tk::anchor1')
    self.htmlview.mark_unset('current')
    self.htmlview.mark_unset('insert')
    
    self._code.save_code(self.htmlview.dump(1.0,'end-1c'))
    
    self.htmlview.mark_set('insert',self.text_insert_position)
    self.htmlview.mark_set('current',self.text_current_position)
    self.render_html_area()
    


  def start(self):
    self.menu()
    self.tools()
    self.htmlview.pack(fill="both", expand=True)
    self.render_html_area()
    self.debugview.pack(fill="both", expand=True)
    self.codeview.pack(fill="both", expand=True)
    self.status.pack(fill="both", side=BOTTOM, expand=True)
    self.root.bind('<KeyPress>', self.on_key_press)
    self.root.mainloop()
