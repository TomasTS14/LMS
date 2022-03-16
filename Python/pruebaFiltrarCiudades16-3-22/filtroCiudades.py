
from utils import *

def writeByAtribute(atributo, nombreAtributo):
    contentHTML = '<html>'
    contentHTML += '<body>'
    ciudades= read('ciudades.xml')
    for ciudad in ciudades:
        if ciudad.attrib[atributo] == nombreAtributo:
            atribNombre = ciudad.attrib['nombre']
            atribPais = ciudad.attrib['pais']
            atribPoblacion = ciudad.attrib['poblacionEnMMM']
            contentHTML += '<p>'+'nombre:'+atribNombre+' pais:'+atribPais+' poblacion:'+atribPoblacion+'</p>'
    contentHTML += '</body>'
    contentHTML += '</html>'
    write('ciudadesFiltradas.html', contentHTML)     


def filtrarPorPais():
    nombrePais = input('Introduce el pais de la ciudad: ')
    writeByAtribute('pais', nombrePais)

def filtrarPorNombre():
    nombreCiudad = input('Introduce el nombre de la ciudad: ')
    writeByAtribute('nombre', nombreCiudad)    

def filtrarPorPoblacion():
    contentHTML = '<html>'
    contentHTML += '<body>'
    ciudades= read('ciudades.xml')
    menor_o_Mayor = int(input('Poblacion mayor que o menor que : \n[1]menor que\n[2]mayor que '))
    numPoblacion = int(input('Esta poblacion (en millones): '))
    if menor_o_Mayor == 1:
        for ciudad in ciudades:
            if int(ciudad.attrib['poblacionEnMMM']) < numPoblacion:
                atribNombre = ciudad.attrib['nombre']
                atribPais = ciudad.attrib['pais']
                atribPoblacion = ciudad.attrib['poblacionEnMMM']
                contentHTML += f'<p>nombre:{atribNombre}, pais:{atribPais}, poblacion:{atribPoblacion} millones</p>'
    elif menor_o_Mayor == 2:
        for ciudad in ciudades:
            if int(ciudad.attrib['poblacionEnMMM']) > numPoblacion:
                atribNombre = ciudad.attrib['nombre']
                atribPais = ciudad.attrib['pais']
                atribPoblacion = ciudad.attrib['poblacionEnMMM']
                contentHTML += f'<p>nombre:{atribNombre}, pais:{atribPais}, poblacion:{atribPoblacion} millones</p>'
    contentHTML += '</body></html>'
    write('CityfiltroPorPoblacion.html', contentHTML)  


def todas():
    contentHTML = '<html>'
    contentHTML += '<body>'
    ciudades= read('ciudades.xml')
    for ciudad in ciudades:
        atribNombre = ciudad.attrib['nombre']
        atribPais = ciudad.attrib['pais']
        atribPoblacion = ciudad.attrib['poblacionEnMMM']
        contentHTML += '<p>'+'nombre: '+ atribNombre + ' pais: ' + atribPais + ' poblacion:' + atribPoblacion + 'M</p>'
    contentHTML += '</body>'
    contentHTML += '</html>'
    write('ciudadesHTML.html', contentHTML)          