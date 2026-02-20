def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def es_par(numero):
    return numero % 2 == 0


def es_mayor_edad(edad):
    return edad >= 18


def saludar(nombre):
    return "Hola, " + nombre


def tipo_numero(numero):
    if numero > 0:
        return "positivo"
    if numero < 0:
        return "negativo"
    return "cero"


def es_palindromo(texto):
    return texto == texto[::-1]


def calcular_media(lista):
    return sum(lista) / len(lista)
