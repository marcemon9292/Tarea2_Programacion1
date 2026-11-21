
# Laboratorio 4 - Ciclos for
# Curso: SOFT-01 - Principios de Programacion I
# Descripcion: Sumar los numeros de una lista utilizando for

lista_numeros = [10, 20, 30, 35, 50, 100, 78, 53, 70, 96, 3222]

def sumatoria_index(lista):
    total = 0 # acumulador, empieza en cero

    for i in range(0, len(lista)):
        total += lista[i] # suma el numero de cada posicion

    return total


print('La suma total es:', sumatoria_index(lista_numeros))
