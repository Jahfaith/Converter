import unittest
from Converter import Convert_temperature, Convert_weight, Convert_currency


class TestConverter(unittest.TestCase):
    '''Unit test for the Convert_temperature class'''
    #def setUp(self):
    def test_celTofah(self):
        result = Convert_temperature.celTofah(20)
        self.assertEqual(result, 68)
        
    def test_kelTocel(self):
        result = Convert_temperature.kelTocel(38)
        self.assertEqual(result, 235.14)
        
    def test_fahTokel(self):
        result = Convert_temperature.fahTokel(14)
        self.assertEqual(result, 263.15)
        
    '''test for the Convert_weight class'''
    def test_kgTogram(self):
        result = Convert_weight.kgTogram(1.2)
        self.assertEqual(result, 1200)
        
    def test_poundsTokg(self):
        result = Convert_weight.poundsTokg(10)
        self.assertEqual(result, 4.536)
        
    def test_gramTopounds(self):
        result = Convert_weight.gramTopounds(40)
        self.assertEqual(result, 0.088)
        
    '''test for the Convert_currency class'''
    def test_nairaTodollar(self):
        result = Convert_currency.nairaTodollar(63000)
        self.assertEqual(result, 152.90)
        
    def test_euroTonaira(self):
        result = Convert_currency.euroTonaira(120)
        self.assertEqual(result, 58192.80)
        
    def test_dollarToeuro(self):
        result = Convert_currency.dollarToeuro(100)
        self.assertEqual(result, 84.74)
        
tests = TestConverter()

tests_loaded = unittest.TestLoader().loadTestsFromModule(tests)

unittest.TextTestRunner().run(tests_loaded)