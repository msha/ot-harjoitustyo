import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):

    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_saldo_oikein(self):
        self.maksukortti = Maksukortti(100)
        self.assertEqual(str(self.maksukortti), "saldo: 1.0")

    def test_ladattu_saldo_oikein(self):
        self.maksukortti = Maksukortti(0)
        self.maksukortti.lataa_rahaa(100)
        self.assertEqual(str(self.maksukortti), "saldo: 1.0")


    def test_ladattu_saldo_oikein_2(self):
        self.maksukortti = Maksukortti(50)
        self.assertEqual(self.maksukortti.ota_rahaa(50), True)
    
    def test_ladattu_saldo_oikein_3(self):
        self.maksukortti = Maksukortti(0)
        self.assertEqual(self.maksukortti.ota_rahaa(50), False)

    def test_ladattu_saldo_oikein_4(self):
        self.maksukortti = Maksukortti(100)
        self.maksukortti.ota_rahaa(150)
        self.assertEqual(str(self.maksukortti), "saldo: 1.0")


    def test_test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)