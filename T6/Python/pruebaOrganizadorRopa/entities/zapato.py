from pruebaOrganizadorRopa.entities.prenda import Prenda


class Zapato(Prenda):

    def __init__(self, marca, color, talla):
        self.tipo = "zapato"
        Prenda.__init__(self, marca, color, talla)
