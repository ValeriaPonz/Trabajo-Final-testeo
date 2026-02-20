# Carolina, Livia y Valeria
# (Protegido con control de excepciones)

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

def saludar(nombre):
    try:
        return "Hola, " + nombre
    except TypeError:
        return "Error: Ingresa un nombre válido en formato texto"

def tipo_numero(numero):
    try:
        if numero > 0:
            return "positivo"
        if numero < 0:
            return "negativo"
        return "cero"
    except TypeError:
        return "Error: Ingresa solo números"

def es_palindromo(texto):
    try:
        # Intenta comprobar si el texto es igual a sí mismo leído al revés
        return texto == texto[::-1]
    except TypeError:
        # Si se le pasa un número o un dato que no se puede "voltear", devuelve False
        return False

def calcular_media(lista):
    try:
        return sum(lista) / len(lista)
    except TypeError:
        return "Error: Ingresa una lista que contenga solo números"
    except ZeroDivisionError:
        # Si la lista está vacía [], len(lista) es 0 y da error al dividir
        return "Error: La lista está vacía, no se puede calcular la media"