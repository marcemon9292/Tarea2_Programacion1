
# Laboratorio 1 - Menu
# Curso: SOFT-01 - Principios de Programacion I
# Descripcion: Cajero automatico con menu de opciones

def cajero_automatico(dinero):
    print('Saldo disponible:', dinero)
    print('1. Depositar')
    print('2. Retirar')
    print('3. Salir')

    opcion = input('Que accion desea hacer?: ')

    match opcion:
        case '1':
            dinero_depositar = int(input('Cuanto va a depositar?: '))
            dinero = dinero + dinero_depositar
            print('Saldo actual:', dinero)

        case '2':
            dinero_retirar = int(input('Cuanto va a retirar?: '))
            if dinero_retirar > dinero:
                print('Saldo insuficiente')
            else:
                dinero = dinero - dinero_retirar
                print('Saldo actual:', dinero)

        case '3':
            print('Saliendo...')

        case _:
            print('Opcion invalida')


cajero_automatico(5000)
