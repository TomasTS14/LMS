from operator import truediv


def saludaA(nombre):
    print(f'Hola {nombre}!')

def suma(a,b):
    return a+b

def esPar(numero):
    if numero % 2 == 0:
        return True
    elif numero % 2 != 0:
        return False

saludaA("Tomas")

print(suma(4,2))

print(esPar(8))
print(esPar(9))

