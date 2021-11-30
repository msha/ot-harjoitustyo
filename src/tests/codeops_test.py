import unittest
from codeops import Code

class Testcodeops(unittest.TestCase):

    def test_init_toimii(self):
        self.assertEqual(Code().read_code(),'<a>testi</a>')
    
    def test_save_toimii(self):
        self.koodi = Code()
        self.koodi.save_code("<h1>toimii jee jee</h1>")
        self.assertEqual(self.koodi.read_code(),'<h1>toimii jee jee</h1>')

    def test_read_toimii(self):
        self.koodi = Code()
        self.assertEqual(self.koodi.read_code(),'<a>testi</a>')