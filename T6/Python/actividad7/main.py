# entities
from common.utils import write
from entities.Armario import Armario
# controllers
from controller.output import writeHTML
from controller.output import writeXML


armario = Armario()
prendas = armario.lee()


def menu():
    seguir = True
    while seguir:
        opcion = input(
            "Elige una opcion:\n1)Mostrar todas las prendas en HTML\n2)Mostrar prenda especifica\n3)insertar una prenda\n4)Borrar una prenda\n5)Salir de la aplicacion\n")
        if opcion == "1":
            file = open('data/output.html', 'r')
            print(file.read())
        elif opcion == "2":
            armario.buscarYmostrarXML()
        elif opcion == "3":
            armario.agregar()
        elif opcion == "4":
            armario.eliminar()
        elif opcion == "5":
            seguir = False
        writeHTML(prendas)
        writeXML(prendas)


menu()
