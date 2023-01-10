# Crear funcionalidad de validar palindromos

def palindromo(palabra: str):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    return palabra_invertida == palabra

def run():
    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra)

    if es_palindromo:
        print('Es un palindromo')
    else:
        print('No es palindromo')


if __name__ == '__main__':
    run()