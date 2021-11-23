import unittest
from fileops import Fileops

class Testfileops(unittest.TestCase):
    

    def test_osaa_kirjoittaa_tiedostoon(self):
        nimi = 'test.html'
        kontentti = 'testi1234'
        file = Fileops()
        file.savefile(nimi,kontentti)

        testfile = open(nimi,"r+").read()
        self.assertEqual(testfile,kontentti)

    def test_osaa_kirjoittaa_tiedoston(self):
        nimi = 'test.html'
        kontentti = 'testi1234'
        file = Fileops()
        file.savefile(nimi,kontentti)
        testfile = open(nimi,"r+")
        self.assertEqual(testfile.name,nimi)


