from common.utils import read
from common.utils import write


def ejercicio1():
    print("Leyendo temperaturas y generando salidas")
    temperaturas = read('data/eltiempo.xml')
    # cabeceras HTML
    contentHTML = '<html>'
    contentHTML += '<body>'
    # recorro las temperaturas
    for lectura in temperaturas:
        elementoHora = lectura.find('hora').tag
        elementoHoraText = lectura.find('hora').text
        elementoGrados = lectura.find('grados').tag
        elementoGradosText = lectura.find('grados').text
        # item en HTML
        contentHTML += '<p>' + elementoHora + ': ' + elementoHoraText + '</p>'
        contentHTML += '<p>' + elementoGrados + ': ' + elementoGradosText + '</p>'
    # cierro el HTML
    contentHTML += '</body>'
    contentHTML += '</html>'
    # escribo en ficheros el contenido formado arriba
    write("temperaturas.html", contentHTML)


def ejercicio2():
    print("Leyendo datos del concesionario")
    coches = read('data/concesionario.xml')
    print("¿Qué coches quieres ver?")
    kmMaximos = int(input("nº máximo de km: "))
    marca = input("Marca: ")
    # cabecera HTML
    contentHTML2 = '<html>'
    contentHTML2 += '<body>'
    # procesar los vehículos y exportar a HTML
    for coche in coches:
        atributoMatricula= coche.attrib['matricula']
        atributoMarca = coche.attrib['marca']
        atributoKM = int(coche.attrib['km'])
        if (atributoMarca == marca) and (atributoKM < kmMaximos):
            contentHTML2 += '<p>' + 'Matricula: ' + atributoMatricula + ' Marca: ' + atributoMarca + ' Kilometros: ' + str(atributoKM) + '<p>'+'<br>'
    contentHTML2 += '</body>'
    contentHTML2 += '</html>'
    write("concesionario.html", contentHTML2)        



def ejercicio3():
    print("Leyendo estudiantes")
    estudiantes = read('data/estudiantes.xml')
    print("¿Qué estudiantes quieres buscar?")
    nombre = input("Nombre: ")
    modulo = input("Algún módulo que curse: ")
    # procesar los estudiantes y exportar a HTML
    contentHTML3 = '<html>'
    contentHTML3 += '<body>'

    alumnoNombre = alumno.attrib['nombre']
    if alumnoNombre == nombre:
        contentHTML3 +='<p>' + ' Alumno: ' + alumnoNombre + '</p>'

        asignaturas = alumno.find("asignaturas")
        asignatura = asignaturas.find("asignatura")

        if(asignatura.attrib["nombre"] == modulo):
            for asignatura in asignaturas:
                contentHTML3 +='<p>' +"Modulo: "+ asignaturaNombre 






    for alumno in estudiantes:
        alumnoNombre = alumno.attrib['nombre']
        if alumnoNombre == nombre:
            asignaturas = alumno.find('asignaturas')
            for asignatura in asignaturas:
                asignaturaNombre = asignatura.attrib['nombre']
                if asignaturaNombre == modulo:
                    contentHTML3 +='<p>' + ' Alumno: ' + alumnoNombre + ' Modulo: '+ asignaturaNombre
    contentHTML3 += '</body>'
    contentHTML3 += '</html>'
    write("estudiantes.html", contentHTML3)


def ejercicio4():
    print("Leyendo productos")
    print("¿Qué productos quieres buscar?")
    nombre = input("Nombre: ")
    mayorMenor = input("Superiores a un precio (si|no): ")
    precio = int(input("Precio: "))
    # procesar los productos y exportar a HTML


def main():
    ejercicio = int(input("nº de ejercicio: "))
    if ejercicio == 1:
        ejercicio1()
    elif ejercicio == 2:
        ejercicio2()
    elif ejercicio == 3:
        ejercicio3()
    elif ejercicio == 4:
        ejercicio4()


main()
