import random
import unittest

from Calculadora import sumar, restar, multiplicar, dividir


class TestFuncionesMasivas(unittest.TestCase):

    def test_sumar_masivo():
        for _ in range(10000):
            a = random.randint(-10**6, 10**6)
            b = random.randint(-10**6, 10**6)
            assert sumar(a, b) == a + b


    def test_restar_masivo():
        for _ in range(10000):
            a = random.randint(-10**6, 10**6)
            b = random.randint(-10**6, 10**6)
            assert restar(a, b) == a - b


    def test_multiplicar_masivo():
        for _ in range(10000):
            a = random.randint(-1000, 1000)
            b = random.randint(-1000, 1000)
            assert multiplicar(a, b) == a * b


    def test_dividir_masivo():
        for _ in range(10000):
            a = random.uniform(-10**6, 10**6)
            b = random.uniform(-10**6, 10**6)
            if b != 0:
                assert dividir(a, b) == a / b


    def test_es_par_masivo():
        for i in range(-100000, 100000):
            assert es_par(i) == (i % 2 == 0)


    def test_es_mayor_edad_masivo():
        for edad in range(0, 150):
            assert es_mayor_edad(edad) == (edad >= 18)

if __name__ == '__main__':
    unittest.main()