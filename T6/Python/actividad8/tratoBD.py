from common.utils import read
import mysql.connector


path = './data/fichero.xml'


class BD:
    mydb = mysql.connector.connect(
        host="192.168.8.25",
        port="3306",
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


    def leer(self):
        self.mycursor.execute("SELECT * FROM camisetas")

        myresult = self.mycursor.fetchall()

        for x in myresult:
            print(x[0]) 
