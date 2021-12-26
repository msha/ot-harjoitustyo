import re
from html.parser import HTMLParser
from string import Template
from bs4 import BeautifulSoup

class HMTLParse(HTMLParser):
    palautus = []
    _tag = ''
    def handle_starttag(self, tag, attrs):
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
        self.bg_color = '#2A2A2A'
        self.fg_color = '#DCDCAA'
        self.boiler = Template('''<!DOCTYPE html>
                        <html lang="en">
                        <head>
                            <title>$title</title>
                            <meta charset="UTF-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1.0">
                            <meta http-equiv="X-UA-Compatible" content="ie=edge">
                            <style>
                                body {  background-color: $bg_color;
                                        color: $fg_color
                                    }
                            </style>
                        </head>
                        <body>
                            $content
                        </body>
                        </html>''')
    def read_code(self):
        return BeautifulSoup(self._code,features="html.parser").prettify()


    def parse_code(self,code_to_parse):
        data = re.sub(r"<.*?a>|<.?html>|<.?body>|[ \t]|[\r\n]|<html.*>(.|\n)*?<\/head>"
            ,"",code_to_parse)
        parser = HMTLParse()
        parser.palautus = []
        parser.feed(data)
        return parser.palautus

    def save_code(self,new_code,title:str):
        '''Parse code to a html format from tkinter text box
        adds proper boiler and variables such as title and background color'''
        self._code = ''
        for (key, value, index) in new_code:
            if key == "tagon" and value in self.validtags:
                self._code += f"<{value}>"
            elif key == "tagoff" and value in self.validtags:
                self._code += f"</{value}>"
            elif key == "tagon" and value == 'justify-center':
                self._code += '<p style="text-align:center;">'
            elif key == "tagoff" and value == 'justify-center':
                self._code += '</p>'
            elif key == "tagon" and value == 'justify-right':
                self._code += '<p style="text-align:right;">'
            elif key == "tagoff" and value == 'justify-right':
                self._code += '</p>'
            elif key == "image":
                self._code += f'<img src="{self.imagepaths[value]}"></img>'
            elif key == "text" and value in('\n'):
                self._code += '<br />'
            elif key == "text" and len(value) > 0 and value != ' ':
                self._code += f'<a>{value}</a>'
        self._code = self.boiler.substitute(title=title,content=self._code,
            bg_color = self.bg_color,fg_color = self.fg_color)

    def codelen(self):
        '''returns length of code without tags'''
        regex = re.compile(r'<.*?>')
        return len(regex.sub('',self._code))+self._code.count('/')
