print('Mensaje')

def imprimir_mensaje():
    print('mensaje especial')
    print('I´m learning Python')

def conversacion(mensaje):
    print('Hola')
    print('Como estas')
    print(mensaje)
    print('Adios')

opcion = int(input("Elige una opciones"))

if opcion == 1:
    conversacion("Eligiste la opción 1")
elif opcion == 2:
    conversacion("Elegiste la opcion 2")
elif opcion == 3:
    conversacion("Eligiste la opcion 3")
else:
    print("Escribe la opcion Incorrecta")