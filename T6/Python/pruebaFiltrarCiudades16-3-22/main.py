from filtroCiudades import *

def main():
    print('Elige una opcion:')
    print('[1]Filtrar por pais')
    print('[2]Filtrar por nombre')
    print('[3]Filtrar por poblacion')
    print('[4] imprimir todas')
    opcion = int(input())

    if opcion == 1:
        filtrarPorPais()
    elif opcion == 2:
        filtrarPorNombre()
    elif opcion == 3:
        filtrarPorPoblacion()
    elif opcion == 4:
        todas()
main()
