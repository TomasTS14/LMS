# entities
from common.utils import write
# controllers
from controller.output import writeHTML
from controller.output import writeXML
from tratoBD import *


def menu():
    bbdd = BD()
    seguir = True
    while seguir == True:
        opcion = int(input(f"Elige una accion:\n" +
                           "1)Leer de fichero y agregar a la base\n" +
                           "2)Generar fichero con datos de la base\n" +
                           "3)mostrar todas las prendas de la BD\n" +
                           "4)agregar prendas\n5)eliminar prendas\n6)Salir de aplicacion\n"))
        if opcion == 1:
            bbdd.leerDeFichero()
        elif opcion == 2:
            bbdd.generarDatosXML('./data/datos.xml')
        elif opcion == 3:
            bbdd.verTodasLasPrendas()
        elif opcion == 4:
            bbdd.agregarPrenda()
        elif opcion == 5:
            bbdd.eliminarPrenda()
        elif opcion == 6:
            seguir = False


menu()
