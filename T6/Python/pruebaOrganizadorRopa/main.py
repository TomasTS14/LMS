from pruebaOrganizadorRopa.entities.armario import Armario


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
    opcion = int(input(
        "Elige filtros a usar: Filtrar por ropa [1]\nfiltrar por color [2]\nfiltrar por talla[3]\nfiltrar por marca [4], Para mostrar resultados[-1]\n"))
    if opcion == 1:
        armario.filtrarPorRopa()
    elif opcion == 2:
        armario.filtrarPorColor()
    elif opcion == 3:
        armario.filtrarPorTalla()
    elif opcion == 4:
        armario.filtrarPorMarca()
    elif opcion == -1:
        armario.mostrarResultados()
