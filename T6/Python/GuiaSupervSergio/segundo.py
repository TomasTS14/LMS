from utils import fechaComparable

class Alumno:
    
    def __init__(self, nombre, anno, mes, dia):
        self.nombre = nombre
        self.fechaNacimiento = f'{dia}/{mes}/{anno}'

    def comparaMayor(self,alumno):
        if fechaComparable(self.fechaNacimiento) > fechaComparable(alumno.fechaNacimiento):
            return True
        else:
            return False


alumnno1 = Alumno('Marcos',2000,11,2)
alumno2 = Alumno('Jorge',1997,2,1)

print(alumno2.comparaMayor(alumnno1))