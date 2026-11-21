
# Laboratorio 6 - Colecciones
# Curso: SOFT-01 - Principios de Programacion I
# Descripcion: Ejercicios con listas del Lab3

# Ejercicio 1 - Encontrar el numero mas pequeno de una lista
# Sin utilizar min()

def numero_mas_pequeno(lista):
    menor = lista[0] # empezamos con el primer numero

    for numero in lista:
        if numero < menor:
            menor = numero

    return menor

numeros = [15, 8, 23, 4, 12]
print('Ejercicio 1')
print('Numero mas pequeno:', numero_mas_pequeno(numeros))

# Ejercicio 2 - Posicion del primer numero no repetido

def primer_no_repetido(lista):
    for i in range(0, len(lista)):
        contador = 0 # contar cuantas veces aparece el numero

        for numero in lista:
            if lista[i] == numero:
                contador += 1

        if contador == 1:
            return i

    return -1 # si todos los numeros se repiten

numeros2 = [3, 5, 3, 7, 5, 9]
print('\nEjercicio 2')
print('Posicion del primer numero no repetido:', primer_no_repetido(numeros2))

# Ejercicio 3 - Cantidad de letras de cada palabra

def contar_letras(palabras):
    cantidades = [] # lista vacia para guardar los resultados

    for palabra in palabras:
        cantidad = len(palabra)
        cantidades.append(cantidad)

    return cantidades

lista_palabras = ['Python', 'Clase', 'Programacion']
print('\nEjercicio 3')
print('Cantidad de letras:', contar_letras(lista_palabras))