from html import entities
from entities.armario import Armario
from entities.prenda import Prenda
from entities.camiseta import Camiseta
from entities.pantalon import Pantalon
from entities.zapato import Zapato


armario = Armario()


def main():
    opcion = int(input(
        "Que deseas hacer:\nAgregar ropa[1]\nFiltrar ropa [2]\nVer toda la ropa [3]\n"))
    match opcion:
        case 1:
            filtrado()
        case 2:
            armario.agregarAarmario()
        case 3:
            armario.verRopaArmario()


def filtrado():
    prendaBuscada = Prenda()
    opcion = int(input(
        "Elige filtros a usar: Filtrar por ropa [1]\nfiltrar por color [2]\nfiltrar por talla[3]\nfiltrar por marca [4], Para mostrar resultados[-1]\n"))
    if opcion == 1:
        tipoRopa = int(
            input("filtra por:\nCamiseta [1]\nPantalon [2]\nZapato [3\n]"))
        match (tipoRopa):
            case 1: prendaBuscada.tipo = "camiseta"
            case 2: prendaBuscada.tipo = "pantalon"
            case 3: prendaBuscada.tipo = "zapato"
    elif opcion == 2:
        colorAbuscar = input("Introduce el color a buscar:\n")
        prendaBuscada.color = colorAbuscar
    elif opcion == 3:
        tallaBuscada = int(input("Introduce la talla que deseas buscar"))
        prendaBuscada.talla = tallaBuscada
    elif opcion == 4:
        marcaBuscada = input("Introduce la marca a buscar")
        prendaBuscada.marca = marcaBuscada
    elif opcion == -1:
        for prenda in armario.prendas:
            if prenda.tipo == prendaBuscada.tipo and prenda.color == prendaBuscada.color and prenda.marca == prendaBuscada.marca:
                print(prenda)
