def run():
    mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }
    print(mi_diccionario['llave1'])
    print(mi_diccionario['llave2'])
    print(mi_diccionario['llave3'])

    poblacion_paises = {
        'Argentina': 44_918_712,
        'Brasil': 210_471_250,
        'Colombia': 50_372_424,
    }

    print(poblacion_paises)

    for pais in poblacion_paises.keys():
        print(pais)

    for pais in poblacion_paises.values():
        print(pais)

    for pais, poblacion in poblacion_paises.items():
        print(pais + " tiene una población de " + str(poblacion) + " habitantes")

if __name__ == '__main__':
    run()
