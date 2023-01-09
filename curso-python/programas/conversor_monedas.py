## Conversor de Monedas

menu = """
    Bienvenido al conversor de moneda ✔

    1. Pesos Colombianos
    2. Pesos Argentinos
    3. Pesos Mexicanos

    Elige una opción: 
"""

def conversion(moneda : str, valor_dolar: float):
    pesos = input("¿Cuántos pesos "+ moneda +" tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")

opcion = int(input(menu))

if opcion == 1:
    conversion("Colombiano", 3500)
elif opcion == 2:
    conversion("Argentinos", 65)
elif opcion == 3:
    conversion("Mexicanos", 24)
else:
    print('Error al digitar la moneda')
