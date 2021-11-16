import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):

    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kortti = Maksukortti(1000)

    def testOletukset(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def testOletukset2(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def testOletukset3(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def testSyoEdukkaastiKateisella(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(240),0)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def testSyoEdukkaasti2Kateisella(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(250),10)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
    
    def testSyoEdukkaasti3Kateisella(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200),200)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def testSyoMaukkaastiKateisella(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(400),0)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
    
    def testSyoMaukkaastiKateisella2(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(440),40)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
    
    def testSyoMaukkaastiKateisella3(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(200),200)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def testSyoEdukkaastiKortilla(self):
        self.kortti = Maksukortti(240)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.kortti),True)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.kortti),False)

    def testSyoMaukkaastiKortilla(self):
        self.kortti = Maksukortti(400)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.kortti),True)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.kortti),False)
    
    def testLataaKortille(self):
        self.kortti = Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(self.kortti,1000)
        self.assertEqual(self.kortti.saldo,1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)
        self.assertFalse(self.kassapaate.lataa_rahaa_kortille(self.kortti,-100))
