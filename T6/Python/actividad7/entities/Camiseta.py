from entities.Prenda import Prenda


class Camiseta(Prenda):
    def __init__(self, marca, color, talla):
        self.tipo = 'camiseta'
        Prenda.__init__(self, marca, color, talla)
