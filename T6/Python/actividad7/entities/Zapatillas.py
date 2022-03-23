from entities.Prenda import Prenda


class Zapatillas(Prenda):
    def __init__(self, marca, color, talla):
        self.tipo = 'zapatillas'
        Prenda.__init__(self, marca, color, talla)
