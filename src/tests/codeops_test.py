import unittest
from codeops import Code

class Testcodeops(unittest.TestCase):

    def setUp(self):
        self.koodi = Code()

    def test_init_toimii(self):
        self.assertEqual(Code().read_code(),'<a>testi</a>')
    
    def test_save_toimii(self):
        self.koodi.save_code("<h1>toimii jee jee</h1>")
        self.assertEqual(self.koodi.read_code(),'<h1>toimii jee jee</h1>')

    def test_read_toimii(self):
        self.assertEqual(self.koodi.read_code(),'<a>testi</a>')
    
    def test_insert_toimii(self):
        self.koodi.insert_code("a")
        self.assertEqual(self.koodi.read_code(),'<a>testi</a>a')
    def test_insert_toimii2(self):   
        self.koodi.insert_code("\x08")
        self.koodi.insert_code("\x08")
        self.koodi.insert_code("\x08")
        self.koodi.insert_code("\x08")
        self.assertEqual(self.koodi.read_code(),'<a>testi')
    def test_insert_toimii3(self):  
        self.koodi.insert_code("\r")
        self.assertEqual(self.koodi.read_code(),'<a>testi</a><br>')
        