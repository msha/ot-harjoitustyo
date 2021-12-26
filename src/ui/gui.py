from tkinter import * #Menu,Frame,PhotoImage,Button,Toplevel,Text,Tk,filedialog,RIGHT,BOTTOM,YES,font,Label
from tkinter.constants import TOP
from tkinter import scrolledtext,font,filedialog
from tkinter.colorchooser import askcolor
import tkinter
from PIL import ImageTk
from logic.codeops import Code
from logic.fileops import Fileops
from logic.database import Database

class CoolButton(tkinter.Button):
    def __init__(self, master, **kw):
        tkinter.Button.__init__(self,master=master,**kw)
        self.configure(bg='#0E0E0E',fg='#BED6FF',relief="flat",highlightthickness=0,padx=15, )
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self.configure(bg='#0E0E0E',fg='#BED6FF',activebackground="#2d2d2d",activeforeground="#D9E577")

    def on_leave(self, e):
        self.configure(bg='#0E0E0E',fg='#BED6FF')

class Gui:

    def __init__(self):

        self.theme_bg = '#1E1E1E'
        self.theme_bg_def = '#2A2A2A'
        self.theme_fcolor = '#BED6FF'
        self.theme_bcolor = '#0E0E0E'
        self.theme_activefg = '#D9E577'

        self.root = Tk()
        self.root.geometry("1280x720")
        self.working_document = 'untitled'
        self.working_document_path = ''
        self.root.title("Editor - "+self.working_document)
        self.root.configure(bg=self.theme_bg,borderwidth = 1)
        self.code_visible = False

        self.current_tag = 'normal'
        self._code = Code()
        self._file = Fileops()
        self._db = Database()
        self.htmlview = scrolledtext.ScrolledText(self.root)
        self.htmlview.configure(bg=self.theme_bg_def,undo=True,fg="#DCDCAA",insertbackground='#D9E577')

        self.text_insert_position = self.htmlview.index('insert')
        self.text_current_position = self.htmlview.index('current')
        
        global images
        images = []

        self.codeview = Text(
            self.root,
            height=6,
            width=40,
            bg=self.theme_bg_def,
            fg="#EFC090"
        )

        #fonts
        h1_font = font.Font(size=36)
        h2_font = font.Font(size=28)
        h3_font = font.Font(size=24)
        h4_font = font.Font(size=18)
        em_font = font.Font(slant='italic')
        strong_font = font.Font(weight='bold')
        self.htmlview.tag_configure("h1", font=h1_font)
        self.htmlview.tag_configure("h2", font=h2_font)
        self.htmlview.tag_configure("h3", font=h3_font)
        self.htmlview.tag_configure("h4", font=h4_font)
        self.htmlview.tag_configure("em", font=em_font)
        self.htmlview.tag_configure("strong", font=strong_font)
        self.htmlview.tag_configure("justify-center", justify='center')
        self.htmlview.tag_configure("justify-right", justify='right')

        self.status_bar = Frame(self.root, bg=self.theme_bg)
        self.status_right = Label(self.status_bar, text = 'adsf',anchor=E, bg=self.theme_bg,fg=self.theme_fcolor) 
        self.status_left = Label(self.status_bar, text = 'adsf',anchor=W, bg=self.theme_bg,fg=self.theme_fcolor) 
        

    def menu(self):
        '''Top menu in GUI'''

        menubar = Menu(self.root,  bg=self.theme_bg,fg=self.theme_fcolor)
        filemenu = Menu(menubar, tearoff=0,bg=self.theme_bg,fg=self.theme_fcolor)
        filemenu.add_command(label="New", command=self.new_document, accelerator="(Ctrl+N)",activebackground=self.theme_bg,activeforeground=self.theme_activefg)
        filemenu.add_command(label="Open", command=self.open_document, accelerator="(Ctrl+O)",activebackground=self.theme_bg,activeforeground=self.theme_activefg)
        open_menu = Menu(filemenu,tearoff=0,bg=self.theme_bg,fg=self.theme_fcolor)
        for row in self._db.get_recent():
            open_menu.add_command(label=row[0], command=lambda n=row[0]: self.open_document(n),activebackground=self.theme_bg,activeforeground=self.theme_activefg)
        filemenu.add_cascade(label="Open recent", menu=open_menu,activebackground=self.theme_bg,activeforeground=self.theme_activefg)
        filemenu.add_command(label="Save", command= self.export_to_file, accelerator="(Ctrl+S)",activebackground=self.theme_bg,activeforeground=self.theme_activefg)
        filemenu.add_command(label="Save as", command= self.export_to_file_and_ask_filename, accelerator="(Ctrl+Shift+S)",activebackground=self.theme_bg,activeforeground=self.theme_activefg)

        filemenu.add_separator()

        filemenu.add_command(label="Exit", command=self.close_program, accelerator="(Ctrl+Q)",activebackground=self.theme_bg,activeforeground=self.theme_activefg)
        menubar.add_cascade(label="File", menu=filemenu,activebackground=self.theme_bg,activeforeground=self.theme_activefg)
        
        editmenu = Menu(menubar, tearoff=0,bg=self.theme_bg,fg=self.theme_fcolor)
        editmenu.add_command(label="Undo", command=self.htmlview.edit_undo, accelerator="(Ctrl+Z)",activebackground=self.theme_bg,activeforeground=self.theme_activefg)
        editmenu.add_command(label="Redo", command=self.htmlview.edit_redo, accelerator="(Ctrl+Shift+Z)",activebackground=self.theme_bg,activeforeground=self.theme_activefg)
        
        menubar.add_cascade(label="Edit", menu=editmenu,activebackground=self.theme_bg,activeforeground=self.theme_activefg)

        viewmenu = Menu(menubar, tearoff=0,bg=self.theme_bg,fg=self.theme_fcolor)
        viewmenu.add_command(label="View HTML", command=self.view_code,activebackground=self.theme_bg,activeforeground=self.theme_activefg)

        menubar.add_cascade(label="View", menu=viewmenu,activebackground=self.theme_bg,activeforeground=self.theme_activefg)

        self.root.config(menu=menubar)

    def export_to_file(self):
        '''Save document to a file
        if file has not been previously saved, jumps to export_to_file_and_ask_filename'''
        if self.working_document != 'untitled':
            self._file.savefile(self.working_document_path,self._code.read_code())
        else:
            self.export_to_file_and_ask_filename()
            self.render_html_area()
        self.menu()

    def export_to_file_and_ask_filename(self):
        '''Asks for a filename and saves document to a given file'''
        self._file.savefile(filedialog.asksaveasfilename(
        filetypes=[("Html documents","*.html")],title="Choose a filename"
        ),self._code.read_code())
        self.working_document = self._file.working_file
        self.working_document_path = self._file.working_file_path
        self.render_html_area()
        self.menu()

    def new_document(self):
        '''Cleansup the current document and start a new'''
        self.htmlview.delete(1.0,'end')
        self._code._code = ''
        self._code.imagepaths = []
        self._file.working_file = ''
        self._file.working_file_path = ''
        self.working_document_path = ''
        self.render_html_area()
    
    def open_document(self,file_to_open=''):
        '''Opens up a HTML for formatting '''
        if file_to_open == '':
            try:
                file_to_open = self._file.openfile(filedialog.askopenfilename(
                filetypes=[("Html documents","*.html")],title='Choose a file'))
            except IOError:
                print("failed to open file")
        else:
            file_to_open = self._file.openfile(file_to_open) 
        raw_html = self._code.parse_code(file_to_open)
        self.working_document = self._file.working_file
        self.working_document_path = self._file.working_file_path
        self.htmlview.delete(1.0,'end')
        for key,value in raw_html:
            self.htmlview.insert("end",key,value)
        self.render_html_area()
    

    def tools(self):
        '''Tool area in GUI'''
        button_frame = Frame(self.root,bg=self.theme_bg)
        button_frame.pack()
        button_frame_2 = Frame(self.root,bg=self.theme_bg)
        button_frame_2.pack()
        bg_icon = PhotoImage(file='./img/background.png')

        self.button_background = CoolButton(
            button_frame,
            text ="Background",
            command = self.bg_color_picker
        )
        h1_button = CoolButton(
            button_frame_2,
            text ="H1",
            command = self.make_h1_tag
        )
        h2_button = CoolButton(
            button_frame_2,
            text ="H2",
            command = self.make_h2_tag
        )
        h3_button = CoolButton(
            button_frame_2,
            text ="H3",
            command = self.make_h3_tag
        )
        h4_button = CoolButton(
            button_frame_2,
            text ="H4",
            command = self.make_h4_tag
        )
        bold_button = CoolButton(
            button_frame,
            text ="Bold",
            command = self.make_strong_tag
        )
        italic_button = CoolButton(
            button_frame,
            text ="Italic",
            command = self.make_em_tag
        )
        justify_center_button = CoolButton(
            button_frame,
            text ="Justify Center",
            command = self.make_center_tag
        )
        justify_right_button = CoolButton(
            button_frame,
            text ="Justify Right",
            command = self.make_right_tag
        )
        add_image = CoolButton(
            button_frame,
            text ="Add Image",
            command = self.create_window_image
            
        )
        self.button_background.grid(row=0,column=0)
        bold_button.grid(row=0,column=1)
        italic_button.grid(row=0,column=2)
        justify_center_button.grid(row=0,column=3)
        justify_right_button.grid(row=0,column=4)
        add_image.grid(row=0,column=5)
        h1_button.grid(row=0,column=1)
        h2_button.grid(row=0,column=2)
        h3_button.grid(row=0,column=3)
        h4_button.grid(row=0,column=4)
        


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
            self._code.save_code(tekstin_syotto.get(1.0,'end'),self._file.working_file)
            window.destroy()

        save = CoolButton(
            window,
            text ="Save",
            command = close
        )
        save.pack(side = BOTTOM)

    def create_window_image(self):
        ''''Window for adding images'''
        window = Toplevel(self.root)
        window.geometry("350x100")
        window.configure(bg=self.theme_bg)
        filepath = Text(
            window,
            height=1,
            width=40,
            bg=self.theme_bg_def,fg=self.theme_activefg
        )
        def open_file():
            filepath.delete(1.0,'end')
            file_path = filedialog.askopenfilename(parent=window,
                filetypes=[("Images","*.jpg *.png *.gif *.webp *.jpeg")],title='Choose a file')
            filepath.insert('end',file_path)

        def close_window():
    
            images.append(ImageTk.PhotoImage(file=filepath.get(1.0,'end-1c')))
            self._code.imagepaths['pyimage'+str(len(images)+1)] = filepath.get(1.0,'end-1c')
            
            self.htmlview.image_create('insert',image=images[len(images)-1])
            window.destroy()
            self.render_html_area()

        browse = CoolButton(
            window,
            text ="Browse images",
            command = open_file
        )
        save = CoolButton(
            window,
            text ="Save",
            command = close_window
        )
        filepath.pack(side=TOP)
        browse.pack(side = LEFT)
        save.pack(side = RIGHT)

    def view_code(self):
        '''View/Hide realtime HTML view at the bottom'''
        self.code_visible = not self.code_visible
        self.render_html_area()
    
    def close_program(self):
        self.root.destroy()

    def bg_color_picker(self):
        color = askcolor(title="Choose the background color")
        self.htmlview.configure(bg=color[1])
        self._code.bg_color = color

    def make_h1_tag(self):
        self.make_tag('h1')
    
    def make_h2_tag(self):
        self.make_tag('h2')
    
    def make_h3_tag(self):
        self.make_tag('h3')
    
    def make_h4_tag(self):
        self.make_tag('h4')
    
    def make_em_tag(self):
        self.make_tag('em')
    
    def make_strong_tag(self):
        self.make_tag('strong')
    
    def make_center_tag(self):
        self.make_tag('justify-center')

    def make_right_tag(self):
        self.make_tag('justify-right')
    
    def make_tag(self,tag):
        tags = self.htmlview.tag_names('sel.first')
        if tag in tags:
            self.htmlview.tag_remove(tag,'sel.first','sel.last')
        else:
            self.htmlview.tag_add(tag,'sel.first','sel.last')
        
        self._code.save_code(self.htmlview.dump(1.0,'end-1c'),self._file.working_file)
        self.render_html_area()
    

        

    def render_html_area(self):
        '''Render of the work in progress HTML'''

        if self.code_visible:
            self.codeview.pack(fill="both", expand=True)
            self.codeview.delete(1.0,'end')
            self.codeview.insert('end',self._code.read_code())
            self.codeview.see('end')
        else:
            self.codeview.pack_forget()

        self.status_right.config(text='code:'+str(len(self._code.read_code()))+' , stripcode:'+str(self._code.codelen())+ ', html len:'+str(len(self.htmlview.get(1.0,'end-1c'))))
        curtags = self.htmlview.tag_names('insert')
        tagstring = ''
        for tag in curtags:
            tagstring += '<'+tag+'>'
        if not curtags:
            tagstring = '<a>'
        self.status_left.config(text='%s'%tagstring)
        self._code.save_code(self.htmlview.dump(1.0,'end-1c'),self._file.working_file)
        self.root.title("Editor - "+self.working_document)

    #doesn't even work btw :D
    dirty_fix_for_double_br = False
    def on_key_press(self,event):
        '''Listing to keyevents and converting them into inputs'''
        if event.keysym == 'Return':
            if self.dirty_fix_for_double_br:
                self.dirty_fix_for_double_br = False
                self.htmlview.insert('insert','\n')
            else:
                self.dirty_fix_for_double_br = True
        elif event.state == 4:
            if event.keysym == 's':
                self.export_to_file()
            if event.keysym == 'n':
                self.new_document()
            if event.keysym == 'o':
                self.open_document()
            if event.keysym == 'q':
                self.close_program()

        elif event.state == 5:
            if event.keysym == 'S':
                self.export_to_file_and_ask_filename()
        
        #save and move insert mark to the end of document temporarily to make parsing easier 
        self.text_insert_position = self.htmlview.index('insert')
        self.htmlview.mark_set('insert','end+1c')
        self.htmlview.mark_set('current','end+1c')
        self.htmlview.mark_unset('tk::anchor1')
        self.htmlview.mark_unset('current')
        self.htmlview.mark_unset('insert')
        
        self.htmlview.mark_set('insert',self.text_insert_position)
        self.htmlview.mark_set('current',self.text_current_position)
        self.render_html_area()
        
    

    def start(self):
        self.menu()
        self.tools()
        self.htmlview.pack(fill="both", expand=True)
        self.render_html_area()
        self.status_bar.pack(side='bottom',fill='both')
        self.status_right.pack(side='right', expand=True,anchor='e')
        self.status_left.pack(fill="both", expand=True,anchor='w')
        self.root.bind('<KeyPress>', self.on_key_press)
        self.root.mainloop()
