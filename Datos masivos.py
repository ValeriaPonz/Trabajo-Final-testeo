import random
from Calculadora import *

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



def test_saludar_masivo():
    for _ in range(5000):
        nombre = ''.join(random.choices("abcdefghijklmnopqrstuvwxyz", k=10))
        assert saludar(nombre) == "Hola, " + nombre


def test_tipo_numero_masivo():
    for i in range(-100000, 100000):
        if i > 0:
            assert tipo_numero(i) == "positivo"
        elif i < 0:
            assert tipo_numero(i) == "negativo"
        else:
            assert tipo_numero(i) == "cero"


def test_es_palindromo_masivo():
    # Palíndromos
    for _ in range(5000):
        base = ''.join(random.choices("abcde", k=5))
        palindromo = base + base[::-1]
        assert es_palindromo(palindromo) is True

    # No palíndromos
    for _ in range(5000):
        texto = ''.join(random.choices("abcdefghijklmnopqrstuvwxyz", k=10))
        if texto != texto[::-1]:
            assert es_palindromo(texto) is False


def test_calcular_media_masivo():
    for _ in range(2000):
        lista = [random.uniform(-1000, 1000) for _ in range(100)]
        assert calcular_media(lista) == sum(lista) / len(lista)