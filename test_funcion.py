# Funciones
import unittest
from Calculadora import sumar
class TestCalculadora(unittest.TestCase):
    def test_sumar_positivos(self):
        self.assertEqual(sumar(2, 3), 5)
        self.assertEqual(sumar(10, 15), 25)

    def test_sumar_negativos(self):
        self.assertEqual(sumar(-2, -3), -5)
        self.assertEqual(sumar(-10, -15), -25)

    def test_restar_positivos(self):
        self.assertEqual(sumar(5, -2), 3)
        self.assertEqual(sumar(15, -10), 5)
    
    def test_restar_negativos(self):
        self.assertEqual(sumar(-5, 2), -3)
        self.assertEqual(sumar(-15, 10), -5)