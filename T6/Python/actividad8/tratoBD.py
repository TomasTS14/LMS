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

    def generarDatosXML(self, fileName):
        content = "<armario>"
        tablas = self.traerTablas()
        tablas = self.arreglaArraysdeStrings(tablas)
        for x in tablas:
            selectActual = f"SELECT * FROM {x}"
            content += f"<{x}>"
            self.mycursor.execute(selectActual)
            prendas = self.mycursor.fetchall()
            for prenda in prendas:
                codigo = prenda[0]
                marca = prenda[1]
                color = prenda[2]
                talla = prenda[3]
                content += f"<{x} codigo='{codigo}' marca='{marca}' color='{color}' talla='{talla}' />"
            content += f"</{x}>"
        content += "</armario>"
        write(fileName, content)

    def arreglaArraysdeStrings(self, array):
        arrayNuevo = []
        contador = 0
        for x in array:
            arrayNuevo.append(array[contador][0])
            contador += 1
        return arrayNuevo

    def verTodasLasPrendas(self):
        self.generarDatosXML('./data/temp.xml')
        file = open('./data/temp.xml')
        contents = file.read()
        print(contents)
        file.close()
        os.remove('./data/temp.xml')

    def agregarPrenda(self):
        tipoPrenda = int(input(
            "Introduce el tipo de prenda a introducir:\nCamiseta [1]\Pantalon [2]\nZapatillas [3]\n"))
        marcaPrenda = input("introduce la marca de esta prenda:\n")
        colorPrenda = input("Introduce el color de la prenda:\n")
        tallaPrenda = input("Introduce la talla de esta prenda:\n")
        print(
            f"La prenda ha introducir es ({tipoPrenda}: marca={marcaPrenda} , color={colorPrenda} , talla={tallaPrenda} ")
        sql = "INSERT INTO %s VALUES (%s, %s, %s)"
        val = (tipoPrenda, marcaPrenda, colorPrenda, tallaPrenda)
        self.mycursor.execute(sql, val)
        self.mydb.commit()

    def eliminarPrenda(self):
        tipoPrenda = int(input(
            "Introduce el tipo de prenda a eliminar:\nCamiseta [1]\Pantalon [2]\nZapatillas [3]\n"))
        marcaPrenda = input("introduce la marca de esta prenda:\n")
        colorPrenda = input("Introduce el color de la prenda:\n")
        tallaPrenda = input("Introduce la talla de esta prenda:\n")
        print(
            f"La prenda ha eliminar es ({tipoPrenda}: marca={marcaPrenda} , color={colorPrenda} , talla={tallaPrenda} ")
        sql = "DELETE FROM %s WHERE marca=%s AND color=%s AND talla=%s"
        val = (tipoPrenda, marcaPrenda, colorPrenda, tallaPrenda)
        self.mycursor.execute(sql, val)
        self.mydb.commit()
