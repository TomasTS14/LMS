def main():
    print('[1]buscar hijo y hermanos')
    print('[2]buscar padre e hijos')
    print('[3]buscar cualquiera')
    opcion = int(input())
    if opcion == 1:
        buscarHijo()
    elif opcion == 2:
        buscarPadre()
    elif buscarCualquiera()