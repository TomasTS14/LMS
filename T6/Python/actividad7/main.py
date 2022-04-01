# entities
from common.utils import write
from entities.Armario import Armario
# controllers
from controller.output import writeHTML
from controller.output import writeXML


armario = Armario()
prendas = armario.lee()
def menu():
    opcion = input("Elige una opcion:\n1)Mostrar todas las prendas en HTML\n2)Mostrar prenda especifica\n3)insertar una prenda\n4)Borrar una prenda\n")
    if opcion == "1":
        file = open('data/output.html', 'r')
        print(file.read())
    elif opcion == "2":
        armario.buscarYmostrarXML()
    elif opcion == "3":
        armario.agregar()
    writeHTML(prendas)
    writeXML(prendas)

menu()