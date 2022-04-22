from entities.camiseta import Camiseta
from entities.pantalon import Pantalon
from entities.prenda import Prenda
from entities.zapato import Zapato
from pathlib import Path
from commons.utils import write, read


class Armario():
    prendas = []

    def __init__(self):
        self.leerArmario()

    def escribeXML(self):
        content = "<armario>"
        for prenda in self.prendas:
            content += f"<{prenda.tipo} marca = {prenda.marca} color = {prenda.color} talla = {prenda.talla}"
        content += "</armario>"
        write(content, "../data/prendas.xml")

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

    def leerArmario(self):
        if Path.exists('data/prendas.xml'):
            prendas = read("../data/prendas.xml")
            for prenda in prendas:
                if prenda.tag == "camiseta":
                    camiseta = Camiseta(
                        prenda.attrib["marca"], prenda.attrib["color"], prenda.attrib["talla"])
                    self.prendas.append(camiseta)
                elif prenda.tag == "pantalon":
                    pantalon = Pantalon(
                        prenda.attrib["marca"], prenda.attrib["color"], prenda.attrib["talla"])
                    self.prendas.append(pantalon)
                elif prenda.tag == "zapato":
                    zapato = Zapato(
                        prenda.attrib["marca"], prenda.attrib["color"], prenda.attrib["talla"])
                    self.prendas.append(zapato)
