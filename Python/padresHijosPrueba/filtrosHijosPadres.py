from utils import *

def buscarHijo():
    menu = True
    while(menu):
        print('Elige opcion')
        print('buscar por nombre.1')
        print('buscar por dni.2')
        print('buscar por grado.3')
        print('salir.4')
        opcion = int(input())
        if opcion == 1:
            nombre = input('Introduce el nombre')
        elif opcion == 2:
            dni = input('Introduce el dni')
        elif opcion == 3:
            grado = input('Introduce el grado')

def buscarPorAtri(atri, nombreAtri):
    padres = read('padresHijos.xml')