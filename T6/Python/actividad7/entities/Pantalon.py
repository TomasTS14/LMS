from entities.Prenda import Prenda


class Pantalon(Prenda):
    def __init__(self, marca, color, talla):
        self.tipo = 'pantalon'
        Prenda.__init__(self, marca, color, talla)
