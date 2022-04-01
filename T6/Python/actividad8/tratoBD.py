from common.utils import read, write
import mysql.connector

path = './data/fichero.xml'


class BD:
    mydb = mysql.connector.connect(
        host="80.34.34.150",
        port="33070",
        user="admin",
        password="admin"

    )
    mycursor = mydb.cursor()

    def leerDeFichero(self):
        prendas = read(path)
        for prenda in prendas:
            self.mycursor.execute(
                f"INSERT INTO {prenda.attrib['tipo']}(marca,color,talla)VALUES({prenda.attrib['marca']},{prenda.attrib['color']},{prenda.attrib['talla']});")
