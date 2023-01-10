

def run():
    LIMITE = 1000
    contador = 0
    potencia_2 = 2 ** contador
    while potencia_2 < LIMITE:
        print('2 Elevado a ' + str(contador) + ' es igual a: ' + str(potencia_2))
        contador = contador + 1
        potencia_2 = 2 ** contador

    for i in range(10):
        print(i)

    say_my_name = input('Say my name: ')
    for letter in say_my_name:
        print(letter.upper())

    print(say_my_name)

if __name__ == '__main__':
    run()