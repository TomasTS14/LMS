from turtle import color
from common.utils import read, write
import mysql.connector
import os

path = './data/fichero.xml'


class BD:
    mydb = mysql.connector.connect(
        host="80.34.34.150",
        port="33070",
        user="actividad8",
        password="actividad8",
        database="armario"
    )
    mycursor = mydb.cursor()

    # LEE DE FICHERO, PUEDE SER UN FICHERO ESPECIFICO, YO TENGO PUESTO UN PREDETERMINADO
    def leerDeFichero(self):
        # path = input("Introduce la ruta del fichero desde el que leer:\n") para leer de ficheros cualquiera, para prueba dejo comentado.
        armario = read(path)
        for prenda in armario:
            tipo = prenda.attrib['tipo']
            marca = prenda.attrib['marca']
            color = prenda.attrib['color']
            talla = prenda.attrib['talla']
            sql = f"INSERT INTO {tipo} (marca, color, talla) VALUES (%s, %s, %s)"
            val = (marca, color, talla)
            self.mycursor.execute(sql, val)
            self.mydb.commit()
        print("Insercion de fichero: "+path+" conseguida\n\n")

    # METODOS AUXILIARES PARA generarDatosXML()
    def leerCada(self, tipo):
        sql = f"SELECT * FROM  {tipo}"

        self.mycursor.execute(sql)

        myresult = self.mycursor.fetchall()
        return myresult

    def traerTablas(self):
        sql = "SHOW TABLES"
        self.mycursor.execute(sql)
        tablas = self.mycursor.fetchall()
        return tablas
    # generarDatosXML()

    def generarDatosXML(self, fileName):
        content = "<armario>"
        tablas = self.traerTablas()
        tablas = self.arreglaArraysdeStrings(tablas)
        for x in tablas:

            prendas = self.leerCada(x)
            content += f"<{x}>"

            for prenda in prendas:

                codigo = prenda[0]
                marca = prenda[1]
                color = prenda[2]
                talla = prenda[3]

                content += f"<{x} codigo='{codigo}' marca='{marca}' color='{color}' talla='{talla}' />"

            content += f"</{x}>"

        content += "</armario>"
        write(fileName, content)

    def verTodasLasPrendas(self):
        self.generarDatosXML('./data/temp.xml')
        file = open('./data/temp.xml')
        contents = file.read()
        print(contents)
        file.close()
        os.remove('./data/temp.xml')

    def agregarPrenda(self):
        tipoPrenda = int(input(
            "Introduce el tipo de prenda a introducir:\nCamiseta [1]\nPantalon [2]\nZapatillas [3]\n"))
        marcaPrenda = input("introduce la marca de esta prenda:\n")
        colorPrenda = input("Introduce el color de la prenda:\n")
        tallaPrenda = input("Introduce la talla de esta prenda:\n")
        match tipoPrenda:
            case 1: tipoPrenda = "camisetas"
            case 2: tipoPrenda = "pantalones"
            case 3: tipoPrenda = "zapatillas"
        print(
            f"La prenda ha introducir es ({tipoPrenda}: marca={marcaPrenda} , color={colorPrenda} , talla={tallaPrenda} ")

        sql = f"INSERT INTO {tipoPrenda} (marca , color , talla) VALUES ('{marcaPrenda}', '{colorPrenda}', '{tallaPrenda}')"
        val = (tipoPrenda, marcaPrenda, colorPrenda, tallaPrenda)
        self.mycursor.execute(sql)
        self.mydb.commit()

    def eliminarPrenda(self):
        tipoPrenda = int(input(
            "Introduce el tipo de prenda a eliminar:\nCamiseta [1]\nPantalon [2]\nZapatillas [3]\n"))
        marcaPrenda = input("introduce la marca de esta prenda:\n")
        colorPrenda = input("Introduce el color de la prenda:\n")
        tallaPrenda = input("Introduce la talla de esta prenda:\n")
        match tipoPrenda:
            case 1: tipoPrenda = "camisetas"
            case 2: tipoPrenda = "pantalones"
            case 3: tipoPrenda = "zapatillas"
        print(
            f"La prenda ha eliminar es ({tipoPrenda}: marca={marcaPrenda} , color={colorPrenda} , talla={tallaPrenda} ")
        sql = "DELETE FROM %s WHERE marca LIKE '%s' AND color LIKE '%s' AND talla LIKE '%s'" % (
            tipoPrenda, marcaPrenda, colorPrenda, tallaPrenda)
        self.mycursor.execute(sql)
        self.mydb.commit()

    def arreglaArraysdeStrings(self, array):
        arrayNuevo = []
        contador = 0
        for x in array:
            arrayNuevo.append(array[contador][0])
            contador += 1
        return arrayNuevo
