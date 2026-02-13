# Funciones
import unittest
from Calculadora import sumar, restar, es_par, es_mayor_edad

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
        self.assertEqual(sumar(-5, 2), -3)
        self.assertEqual(sumar(-15, 10), -5)

        self.assertEqual(restar(-5, 2), -7)
        self.assertEqual(restar(-15, 10), -25)

    def test_multipicacion_basica(self):
        self.assertEqual (multiplicar(2,3),6)
        self.assertEqual (multiplicar (-2,-3),6)

    def tet_division_basica (self):
        self.assertEqual (dividir(8,2),4)
        self.assertEqual (dividir(-8, -2),4)

    def test_es_par_positivos(self):
        self.assertTrue(es_par(2))
        self.assertTrue(es_par(4))

    def test_es_par_negativos(self):
        self.assertTrue(es_par(-2))
        self.assertTrue(es_par(-8))
    
    def test_es_mayor_edad_positivos(self):
        self.assertTrue(es_mayor_edad(20))
        self.assertTrue(es_mayor_edad(19))
    
    def test_es_mayor_edad_negativos(self):
        self.assertFalse(es_mayor_edad(10))
        self.assertFalse(es_mayor_edad(15))

if __name__ == '__main__':
    unittest.main()
