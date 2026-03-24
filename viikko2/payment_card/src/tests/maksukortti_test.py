# src/tests/maksukortti_test.py
import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.kortti = Maksukortti(1000)  # 10.00 €

    def test_constructor_sets_balance_correctly(self):
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 10.00 euroa")

    def test_constructor_fail_example(self):
        # deliberately wrong expected value to see the test fail
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 9.00 euroa")

    def test_syo_edullisesti_vahentaa_saldoa_oikein(self):
        self.kortti.syo_edullisesti()  # costs 2.50 €
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 7.50 euroa")

    def test_syo_maukkaasti_vahentaa_saldoa_oikein(self):
        self.kortti.syo_maukkaasti()  # costs 4.00 €
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 6.00 euroa")

    def test_lataa_rahaa_kasvattaa_saldoa_oikein(self):
        self.kortti.lataa_rahaa(500)  # add 5.00 €
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 15.00 euroa")

    def test_lataa_rahaa_negatiivinen_ei_muuta_saldoa(self):
        self.kortti.lataa_rahaa(-100)  # invalid load
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 10.00 euroa")

    def test_lataa_rahaa_ei_ylita_maksimia(self):
        self.kortti.lataa_rahaa(20000)  # try to go over 150.00 €
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 150.00 euroa")

    def test_hello_world(self):
        self.assertEqual("Hello world", "Hello world")

if __name__ == "__main__":
    unittest.main()
