# entities
from entities.Armario import Armario
# controllers
from controller.output import writeHTML
from controller.output import writeXML

armario = Armario()


prendas = armario.lee()

armario.agregar()

writeHTML(prendas)
writeXML(prendas)
