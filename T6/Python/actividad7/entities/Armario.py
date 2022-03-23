
from common.utils import read
# prendas
from entities.Camiseta import Camiseta
from entities.Pantalon import Pantalon
from entities.Zapatillas import Zapatillas

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
        
        tipo = int(input("Que deseas agregar \n1)Camiseta\n2)Pantalon\n3)Zapatillas"))
        if tipo == 1:
            marca = input("Introduce la marca:")
            color = input ("Introduce el color:")
            talla = input("Introduce la talla")
            prenda = Camiseta(marca,color,talla)
        elif tipo == 2:
            marca = input("Introduce la marca:")
            color = input ("Introduce el color:")
            talla = input("Introduce la talla")
            prenda = Pantalon(marca,color,talla)
        elif tipo == 3:
            marca = input("Introduce la marca:")
            color = input ("Introduce el color:")
            talla = input("Introduce la talla")
            prenda = Zapatillas(marca,color,talla)

        self.prendas.append(prenda)

    def eliminar(self):
        for prenda in prendas:
            