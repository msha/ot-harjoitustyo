import unittest
from logic.codeops import Code

class TestCodeops(unittest.TestCase):

    def setUp(self):
        self.koodi = Code()
        self.koodi.imagepaths = {'pyimage2': '/mnt/c/koulu/ohte/ot-harjoitustyo/img/kisse.gif'}
        self.testikoodi = [('mark', 'current', '1.0'), ('tagon', 'h1', '1.0'), ('text', 'Otsikko', '1.0'), ('tagoff', 'h1', '1.7'), ('text', '\n', '1.7'), ('image', 'pyimage2', '2.0'), ('mark', 'insert', '2.1'), ('text', '\n', '2.1'), ('tagon', 'strong', '3.0'), ('text', 'bold', '3.0'), ('tagoff', 'strong', '3.4'), ('text', ' ja ', '3.4'), ('tagon', 'em', '3.8'), ('text', 'italic', '3.8'), ('tagoff', 'em', '3.14'), ('text', '\n', '3.14'), ('text', '\n', '4.0'), ('tagon', 'justify-center', '5.0'), ('text', 'center', '5.0'), ('tagoff', 'justify-center', '5.6'), ('text', '\n', '5.6'), ('text', '\n', '6.0'), ('tagon', 'justify-right', '7.0'), ('text', 'right', '7.0')]

    def test_save(self):

        self.koodi.save_code(self.testikoodi,'testititle1234')
        self.assertIn('<title>testititle1234</title>',self.koodi._code)
        self.assertIn('background-color: #2A2A2A;',self.koodi._code)
        self.assertIn('color: #DCDCAA',self.koodi._code)
        self.assertIn('</p>',self.koodi._code)
        self.assertIn('<p style="text-align:right;">',self.koodi._code)
        self.assertIn('<p style="text-align:center;">',self.koodi._code)
        self.assertIn('<br />',self.koodi._code)
        self.assertNotIn('tagon',self.koodi._code)
        self.assertNotIn('tagoff',self.koodi._code)
    
    def test_parse_code(self):
        parsittava = 