from common.utils import read, write
import mysql.connector


path = './data/fichero.xml'
pathSalida = './data/datos.xml'


class BD:
    mydb = mysql.connector.connect(
        host="192.168.8.25",
        port="3306",
        user="actividad8",
        password="actividad8",
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


    def leerCada(self,tipo):
        sql = f"SELECT * FROM  {tipo}"
        
        self.mycursor.execute(sql)

        myresult = self.mycursor.fetchall()
        return myresult

    def traerTablas(self):
        sql = "SHOW TABLES"
        self.mycursor.execute(sql)
        tablas = self.mycursor.fetchall()
        return tablas

    def escribirDatosXML(self):
        content = "<armario>" 
        tablas = self.traerTablas()
        for x in tablas:
            selectActual = f"SELECT * FROM {x}"
            content += f"<{x}>"
            self.mycursor.execute(selectActual)
            prendas = self.mycursor.fetchall()
            for prenda in prendas:
                marca = prenda[0]
                color = prenda[1]
                talla = prenda[2]
                content += f"<{x} marca='{marca}' color = '{color}' talla='{talla}/>"
            content += f"<{x}/>"
        content += "</armario>"
        write(pathSalida,content)
