
# Laboratorio 3 - Ciclos while
# Curso: SOFT-01 - Principios de Programacion I
# Descripcion: Contar numeros desde 1 hasta un numero indicado

def contar_hasta(tope):
    contador = 1 #punto de inicio (bucle, necesita saber en que valor empieza y que termina)

    while(contador <= tope):
        print(contador)
        contador += 1


contar_hasta(6)
