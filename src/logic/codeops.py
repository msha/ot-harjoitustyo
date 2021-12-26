import re
from bs4 import BeautifulSoup
from html.parser import HTMLParser

class HMTLParse(HTMLParser):
    palautus = []
    _tag = ''
    def handle_starttag(self, tag, attr):
        self._tag = tag

    def handle_endtag(self, tag):
        if tag == 'br':
            line = ['\n','']
            self.palautus.append(line)

    def handle_data(self, data):
        tag = self._tag
        if tag == 'br':
            tag = ''
        line = [data,tag]
        self.palautus.append(line)

class Code:
    '''Handles behind the scenes code manipulations
    so that actions are interpreted as they should'''
    def __init__(self,code = '<a>testi</a>'):
        self._code = code
        self.imagepaths = {}
        self.validtags = ['br','a','h1','img','p','h2','h3','h4','strong','em','ul','ol']

    def read_code(self):
        return BeautifulSoup(self._code,features="html.parser").prettify()


    def parse_code(self,code_to_parse):
        data = re.sub(r"<.*?a>|<.?html>|<.?body>|[ \t]|[\r\n]","",code_to_parse)
        parser = HMTLParse()
        parser.palautus = []
        parser.feed(data)
        return parser.palautus

    def save_code(self,new_code):
        self._code = ''
        for (key, value, index) in new_code:
            print(key+'  : '+value+' : '+index)
            if key == "tagon" and value in self.validtags:
                self._code += f"<{value}>"
            elif key == "tagoff" and value in self.validtags:
                self._code += f"</{value}>"
            elif key == "image":
                self._code += f'<img src="{self.imagepaths[value]}"></img>'
            elif key == "text" and value in('\n'):
                self._code += '<br />'
            elif key == "text" and len(value) > 0 and value != ' ':
                self._code += f'<a>{value}</a>'

    def insert_code(self,new_code):
        self._code += new_code

    def codelen(self):
        regex = re.compile(r'<.*?>')
        return len(regex.sub('',self._code))+self._code.count('/')


    def special_command(self,event):
        '''Read special characters and convert them into an appropriate action'''
        def backspace():
            pass

        def enter():
            self.insert_code('</br>')

        def space():
            self.insert_code(' ')

        command={
            'BackSpace': backspace,
            'Return': enter,
            'space': space
        }
        if event in command:
            command.get(event)()
