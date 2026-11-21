
# Laboratorio 5 - Menu con while True
# Curso: SOFT-01 - Principios de Programacion I
# Descripcion: Menu interactivo para crear una lista de compras

'''
hacer un menu dinamico, que pueda agregar productos para una lista de compras.
1. Agregar producto a la lista.
2. Mostrar la lista.
3. Salir.
'''

def crear_lista_de_compras():
    print('Bienvenido al sistema de creacion de listas de compras')
    lista = ""  # se guardan los strings que agrego, cada uno es un producto que necesito comprar. La lista empieza vacia

    while (True):
        print('1. Agregar producto a la lista')
        print('2. Mostrar la lista')
        print('3. Salir')

        opcion = input('Cual opcion quiere hacer?: ')

        match opcion:
            case "1":
                producto = input("Cual producto quiere agregar?: ")
                lista += (producto + '\n')

            case "2":
                print(lista)

            case "3":
                break

            case _:
                print('Opcion no valida')


crear_lista_de_compras()
