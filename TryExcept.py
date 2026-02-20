import random
import unittest

from Calculadora import sumar, restar, multiplicar, dividir, es_par, es_mayor_edad
class TestTryExcept(unittest.TestCase):

    def sumar(a, b):
        try:
            return a + b
        except TypeError:
            return "Error: Ingresa solo números"

    def restar(a, b):
        try:
            return a - b
        except TypeError:
            return "Error: Ingresa solo números"

    def multiplicar(a, b):
        try:
            return a * b
        except TypeError:
            return "Error: Ingresa solo números"

    def dividir(a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Error: No se puede dividir entre cero"
        except TypeError:
            return "Error: Ingresa solo números"

    def es_par(numero):
        try:
            return numero % 2 == 0
        except TypeError:
            return False

    def es_mayor_edad(edad):
        try:
            return edad >= 18
        except TypeError:
            return False
if __name__ == '__main__':
    unittest.main()