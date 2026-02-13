# Funciones
import unittest
from Calculadora import sumar, restar

class sTestCalculadora(unittest.TestCase):
    def test_sumar_positivos(self):
        self.assertEqual(sumar(2, 3), 5)
        self.assertEqual(sumar(10, 15), 25)

    def test_sumar_negativos(self):
        self.assertEqual(sumar(-2, -3), -5)
        self.assertEqual(sumar(-10, -15), -25)
        
    def test_restar_positivos(self):
        self.assertEqual(restar(5, -2), 7)
        self.assertEqual(restar(15, -10), 25)
    
    def test_restar_negativos(self):
        self.assertEqual(restar(-5, 2), -7)
        self.assertEqual(restar(-15, 10), -25)

if __name__ == '__main__':
    unittest.main()