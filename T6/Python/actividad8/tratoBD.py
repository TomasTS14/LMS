from common.utils import read
import mysql.connector


path = './data/fichero.xml'


class BD:
    mydb = mysql.connector.connect(
        host="80.34.34.150",
        port="33070",
        user="admin",
        password="admin",
        database="armario"
    )
    mycursor = mydb.cursor()

    def leerDeFichero(self):
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


def generarFicherConBD(self):
