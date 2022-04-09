from pruebaOrganizadorRopa.entities.camiseta import Camiseta
from pruebaOrganizadorRopa.entities.pantalon import Pantalon
from pruebaOrganizadorRopa.entities.prenda import Prenda
from pruebaOrganizadorRopa.entities.zapato import Zapato


class Armario():
    prendas = []

    def escribeXML(self):
        content = "<armario>"
        for prenda in self.prendas:
            content += f"<{prenda.tipo} marca = {prenda.marca} color = {prenda.color} talla = {prenda.talla}"
        content += "</armario>"

    def agregarAarmario(self):
        prendaAagregar = None
        tipo = int(input(
            "especifica el tipo de prenda que vas a agregar\nCamiseta [1]\nPantalon [2]\nZapato[3]\n"))
        match tipo:
            case 1:
                prendaAagregar = Camiseta()
            case 2:
                prendaAagregar = Pantalon()
            case 3:
                prendaAagregar = Zapato()
        prendaAagregar.marca = input(
            f"introduce la marca de {prendaAagregar.tipo}")
        prendaAagregar.color = input(f"introduce el color de la prenda")
        prendaAagregar.talla = input(
            f"introduce la talla de {prendaAagregar.tipo}")
        self.prendas.append(prendaAagregar)
        self.escribeXML()
