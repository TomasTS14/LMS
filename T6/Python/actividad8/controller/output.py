
from common.utils import write


def writeHTML(prendas):
    htmlContent = '<html><body>'
    for prenda in prendas:
        htmlContent += '<div>'
        htmlContent += '<p>'+prenda.tipo+'</p>'
        htmlContent += '<p>'+prenda.marca+'</p>'
        htmlContent += '<p>'+prenda.color+'</p>'
        htmlContent += '<p>'+prenda.talla+'</p>'
        htmlContent += '</div>'
    htmlContent += '</body></html>'
    write('./data/output.html', htmlContent)


def writeXML(prendas):
    htmlContent = '<armario>'
    for prenda in prendas:
        htmlContent += '<prenda '
        htmlContent += 'tipo="'+prenda.tipo+'" '
        htmlContent += 'marca="'+prenda.marca+'" '
        htmlContent += 'color="'+prenda.color+'" '
        htmlContent += 'talla="'+prenda.talla+'" '
        htmlContent += ' />'
    htmlContent += '</armario>'
    write('./data/output.xml', htmlContent)
