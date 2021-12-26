from tkinter import * #Menu,Frame,PhotoImage,Button,Toplevel,Text,Tk,filedialog,RIGHT,BOTTOM,YES,font,Label
from tkinter.constants import INSERT, TOP
from tkinter import scrolledtext,font,filedialog
from PIL import ImageTk
from logic.codeops import Code
from logic.fileops import Fileops
from logic.database import Database

class Gui:

    def __init__(self):
        self.root = Tk()
        self.root.geometry("1280x720")
        self.working_document = 'untitled'
        self.root.title("Editor - "+self.working_document)

        self._code = Code()
        self._file = Fileops()
        self._db = Database()
        self.htmlview = scrolledtext.ScrolledText(self.root)
        self.htmlview.configure(bg='white',undo=True)

        self.text_insert_position = self.htmlview.index('insert')
        self.text_current_position = self.htmlview.index('current')
        
        self.debugview = Text(
            self.root,
            height=6,
            width=40
        )
        global images
        images = []

        self.codeview = Text(
            self.root,
            height=6,
            width=40
        )

        #fonts
        h1_font = font.Font(size=36)
        self.htmlview.tag_configure("h1", font=h1_font)

        self.status_bar = Frame(self.root)
        self.status_right = Label(self.status_bar, text = 'adsf',anchor=E) 
        self.status_left = Label(self.status_bar, text = 'adsf',anchor=W) 
        

    def menu(self):
        '''Top menu in GUI'''

        menubar = Menu(self.root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.new_document, accelerator="(Ctrl+N)")
        filemenu.add_command(label="Open", command=self.open_document, accelerator="(Ctrl+O)")
        open_menu = Menu(filemenu,tearoff=0)
        for row in self._db.get_recent():
            print(row[0])
            open_menu.add_command(label=row[0], command=lambda n=row[0]: self.open_document(n))
        filemenu.add_cascade(label="Open recent", menu=open_menu)
        filemenu.add_command(label="Save", command= self.export_to_file, accelerator="(Ctrl+S)")
        filemenu.add_command(label="Save as", command= self.export_to_file_and_ask_filename, accelerator="(Ctrl+Shift+S)")

        filemenu.add_separator()

        filemenu.add_command(label="Exit", command=self.close_program, accelerator="(Ctrl+Q)")
        menubar.add_cascade(label="File", menu=filemenu)
        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Undo", command=self.htmlview.edit_undo, accelerator="(Ctrl+Z)")
        editmenu.add_command(label="Redo", command=self.htmlview.edit_redo, accelerator="(Ctrl+Shift+Z)")
        menubar.add_cascade(label="Edit", menu=editmenu)

        self.root.config(menu=menubar)

    def export_to_file(self):
        if self.working_document != 'untitled':
            Fileops.savefile(self.working_document,self._code.read_code())
        else:
            self.export_to_file_and_ask_filename()
            self.render_html_area()
        self.menu()

    def export_to_file_and_ask_filename(self):
        self._file.savefile(filedialog.asksaveasfilename(
        filetypes=[("Html documents","*.html")],title="Choose a filename"
        ),self._code.read_code())
        self.working_document = self._file.working_file
        self.render_html_area()
        self.menu()

    def new_document(self):
        self.htmlview.delete(1.0,'end')
        self.render_html_area()
    
    def open_document(self,file_to_open=''):
        print('avaan:'+file_to_open)
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
        self.htmlview.delete(1.0,'end')
        for key,value in raw_html:
            self.htmlview.insert("end",key,value)
        self.render_html_area()

    def tools(self):
        '''Tool area in GUI'''
        button_frame = Frame(self.root)
        button_frame.pack()
        bg_icon = PhotoImage(file='./img/background.png')

        self.button_background = Button(
            button_frame,
            text ="Background",
            command = ''
        )
        self.button_background.pack(side = RIGHT)
        view_code = Button(
            button_frame,
            text ="Code",
            command = self.create_window_code
        )
        view_code.pack(side = RIGHT,expand=YES)
        text_tools = Button(
            button_frame,
            text ="Text",
            command = self.create_window_code
        )
        text_tools = Button(
            button_frame,
            text ="H1",
            command = self.make_h1_tag
        )
        redo_button = Button(
            button_frame,
            text ="Redo",
            command = self.htmlview.edit_redo
        )
        redo_button.pack(side=LEFT,expand=YES)
        undo_button = Button(
            button_frame,
            text ="Undo",
            command = self.htmlview.edit_undo
        )
        undo_button.pack(side=LEFT)
        text_tools.pack(side = RIGHT,expand=YES)
        add_image = Button(
            button_frame,
            text ="Add Image",
            command = self.create_window_image
        )
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
            command = close
        )
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

            browse = Button(
                window,
                text ="Browse images",
                command = open_file
            )
            save = Button(
                window,
                text ="Save",
                command = close_window
            )
            filepath.pack(side=TOP)
            browse.pack(side=TOP,pady=20)
            save.pack(side = BOTTOM)
    
    def close_program(self):
        self.root.destroy()

    def make_h1_tag(self):
        tags = self.htmlview.tag_names('sel.first')
        if "h1" in tags:
            self.htmlview.tag_remove("h1",'sel.first','sel.last')
        else:
            self.htmlview.tag_add("h1",'sel.first','sel.last')
        
        self._code.save_code(self.htmlview.dump(1.0,'end-1c'))
        self.render_html_area()
        

    def render_html_area(self):
        '''Render of the work in progress HTML'''

        self.debugview.delete(1.0,'end')
        self.debugview.insert('end',self.htmlview.dump(1.0,'end', tag=True, text=True))

        self.codeview.delete(1.0,'end')
        self.codeview.insert('end',self._code.read_code())

        self.status_right.config(text='code:'+str(len(self._code.read_code()))+' , stripcode:'+str(self._code.codelen())+ ', html len:'+str(len(self.htmlview.get(1.0,'end-1c'))))
        curtags = self.htmlview.tag_names('insert')
        tagstring = ''
        for tag in curtags:
            tagstring += '<'+tag+'>'
        if not curtags:
            tagstring = '<a>'
        self.status_left.config(text='%s'%tagstring)
        self._code.save_code(self.htmlview.dump(1.0,'end-1c'))
        self.root.title("Editor - "+self.working_document)

    dirty_fix_for_double_br = False
    def on_key_press(self,event):
        '''Listing to keyevents and converting them into inputs'''
        print(str(event.state)+' '+event.keysym)
        if event.keysym == 'Return':
            if self.dirty_fix_for_double_br:
                self.dirty_fix_for_double_br = False
                self.htmlview.insert('insert','\n')
            else:
                self.dirty_fix_for_double_br = True
        #state 4 = ctrl
        elif event.state == 4:
            if event.keysym == 's':
                self.export_to_file()
            if event.keysym == 'n':
                self.new_document()
            if event.keysym == 'o':
                self.open_document()
            if event.keysym == 'q':
                self.close_program()

        # state 5 = ctrl + shift
        elif event.state == 5:
            if event.keysym == 's':
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
        self.debugview.pack(fill="both", expand=True)
        self.codeview.pack(fill="both", expand=True)
        self.status_bar.pack(fill='both')
        self.status_right.pack(side='right', expand=True,anchor='e')
        self.status_left.pack(fill="both", expand=True,anchor='w')
        self.root.bind('<KeyPress>', self.on_key_press)
        self.root.mainloop()
