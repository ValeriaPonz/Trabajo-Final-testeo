def sumar(a, b):
    try:
        return a + b
    except TypeError:
        return "Error: suma"


def restar(a, b):
    try:
        return a - b
    except TypeError:
        return "Error: resta"


def multiplicar(a, b):
    try:
        return a * b
    except TypeError:
        return "Error: multiplicación"


def dividir(a, b):
    try:
        return a / b
    except TypeError:
        return "Error: división"
    except ZeroDivisionError:  
        return "Error: división por cero"


def es_par(numero):
    try:
        return numero % 2 == 0
    except TypeError:
        return "Error: paridad"


def es_mayor_edad(edad):
    try:
        return edad >= 18
    except TypeError:
        return "Error: edad"


def saludar(nombre):
    try:
        return "Hola, " + nombre
    except TypeError:
        return "Error: saludo"
    

def tipo_numero(numero):
    try:
        if numero > 0:
            return "positivo"
        if numero < 0:
            return "negativo"
    except TypeError:
        return "Error: cero"


def es_palindromo(texto):
    return texto == texto[::-1]


def calcular_media(lista):
    return sum(lista) / len(lista)
