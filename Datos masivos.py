import random

ERROR = -9999

def sumar(a, b):
    try:
        return a + b
    except:
        return ERROR

def dividir(a, b):
    try:
        return a / b
    except:
        return ERROR

def es_par(numero):
    try:
        return 1 if numero % 2 == 0 else 0
    except:
        return ERROR

def calcular_media(lista):
    try:
        return sum(lista) / len(lista)
    except:
        return ERROR


# === TEST MASIVO ===

errores = 0
pruebas = 10000   # cantidad de pruebas

for _ in range(pruebas):
    
    # Generar datos aleatorios 
    a = random.choice([random.randint(-100, 100), "texto", None])
    b = random.choice([random.randint(-100, 100), 0, "error"])
    
    resultado = sumar(a, b)
    if resultado == ERROR:
        errores += 1

    resultado = dividir(a, b)
    if resultado == ERROR:
        errores += 1

    resultado = es_par(a)
    if resultado == ERROR:
        errores += 1

    lista = random.choice([
        [random.randint(1, 10) for _ in range(random.randint(0, 5))],
        [],
        "lista mala"
    ])

    resultado = calcular_media(lista)
    if resultado == ERROR:
        errores += 1


print("Total de pruebas realizadas:", pruebas * 4)
print("Total de errores detectados:", errores)