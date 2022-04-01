
from common.utils import read, write
# prendas
from entities.Camiseta import Camiseta
from entities.Pantalon import Pantalon
from entities.Zapatillas import Zapatillas
import entities.Prenda
path = './data/datos.xml'


class Armario:
    prendas = []

    def lee(self):
        datos = read(path)
        for prendaData in datos:
            marca = ''
            tipo = prendaData.attrib['tipo']
            if 'marca' in prendaData.attrib:
                marca = prendaData.attrib['marca']
            color = prendaData.attrib['color']
            talla = prendaData.attrib['talla']
            prenda = None
            if tipo == 'camiseta':
                prenda = Camiseta(marca, color, talla)
            elif tipo == 'pantalon':
                prenda = Pantalon(marca, color, talla)
            elif tipo == 'zapatillas':
                prenda = Zapatillas(marca, color, talla)
            self.prendas.append(prenda)
        return self.prendas

    def agregar(self):

        tipo = int(
            input("Que deseas agregar \n1)Camiseta\n2)Pantalon\n3)Zapatillas\n"))
        if tipo == 1:
            marca = input("Introduce la marca:")
            color = input("Introduce el color:")
            talla = input("Introduce la talla:")
            prenda = Camiseta(marca, color, talla)
        elif tipo == 2:
            marca = input("Introduce la marca:")
            color = input("Introduce el color:")
            talla = input("Introduce la talla:")
            prenda = Pantalon(marca, color, talla)
        elif tipo == 3:
            marca = input("Introduce la marca:")
            color = input("Introduce el color:")
            talla = input("Introduce la talla:")
            prenda = Zapatillas(marca, color, talla)

        self.prendas.append(prenda)

    def buscarYmostrarXML(self):
        contentXML = "<armario>"
        tipoPrenda = input(
            "Que tipo de prenda quieres buscar:\n1)Camiseta\n2)Pantalon\n3)Zapatilla\n")
        if tipoPrenda == "1":
            tipoPrenda = "camiseta"
        elif tipoPrenda == "2":
            tipoPrenda = "pantalon"
        elif tipoPrenda == "3":
            tipoPrenda = "zapatillas"
        atribABuscar = input(
            "Por qué atributo deseas buscar:\n1)Marca\n2)Color\n3)Talla\n")
        atribNombre = input("Introduce el dato")

        for prenda in self.prendas:
            if prenda.tipo == tipoPrenda and atribABuscar == "1":
                print("encontrado")
                if prenda.marca == atribNombre:
                    contentXML += f'<prenda tipo="{prenda.tipo}" marca="{prenda.marca}" color="{prenda.color}" talla ="{prenda.talla}" />'
            if prenda.tipo == tipoPrenda and atribABuscar == "2":
                if prenda.color == atribNombre:
                    contentXML += f'<prenda tipo="{prenda.tipo}" marca="{prenda.marca}" color="{prenda.color}" talla ="{prenda.talla}" />'
            if prenda.tipo == tipoPrenda and atribABuscar == "3":
                if prenda.talla == atribNombre:
                    contentXML += f'<prenda tipo="{prenda.tipo}" marca="{prenda.marca}" color="{prenda.color}" talla ="{prenda.talla}" />'
        contentXML += "</armario>"
        write("data/resultados.xml", contentXML)
        file = open("data/resultados.xml", "r")
        print(file.read())

    def eliminar(self):
        tipoPrenda = input(
            "Elige el tipo de prenda que quieres eliminar\n1)Camiseta\n2)Pantalon\n3)Zapatillas\n")
        if tipoPrenda == "1":
            tipoPrenda = "camiseta"
        elif tipoPrenda == "2":
            tipoPrenda = "pantalon"
        elif tipoPrenda == "3":
            tipoPrenda = "zapatillas"
        atribABuscar = input(
            "Por que atributo deseas buscar: \n1)Marca\n2)Color\n3)Talla\n")
        nombreAtributo = input("Introduce el dato:")
        for prenda in self.prendas:
            if prenda.tipo == tipoPrenda and atribABuscar == "1":
                if prenda.marca == nombreAtributo:
                    self.prendas.remove(prenda)
            if prenda.tipo == tipoPrenda and atribABuscar == "2":
                if prenda.color == nombreAtributo:
                    self.prendas.remove(prenda)
            if prenda.tipo == tipoPrenda and atribABuscar == "3":
                if prenda.talla == nombreAtributo:
                    self.prendas.remove(prenda)
