# Ejercicio 3 ~ Administracion de estacionamiento (ejercicio3_estacionamiento.py / Version 1)
# Curso: SOFT-01 - Principios de Programación I
# Autor: Marcela Otárola
# Fecha: 11/11/2026
# Descripción: Programa para administrar entradas, salidas y cobros de un estacionamiento.

print('Sistema de administracion de estacionamiento')

# Variables
capacidad = 20  # espacios
tarifa = 800 # colones
vehiculos_actuales = 0 # 	Contador de vehículos que están estacionados.
total_entradas = 0 # Contador de vehículos que han ingresado.
total_salidas = 0 #Contador de vehículos salieron.
total_ingresos = 0 # Acumulador del dinero que se ha cobrado.

# Menu principal
while True:
    print('\n--- MENU DE ESTACIONAMIENTO ---')
    print('1. Registrar entrada de vehiculo')
    print('2. Registrar salida de vehiculo')
    print('3. Consultar ocupacion')
    print('4. Consultar recaudacion')
    print('5. Salir')

    opcion = input('Seleccione una opcion: ')

    match opcion:
        # Caso 1: Registrar entrada
        case '1':
            if vehiculos_actuales < capacidad:
                vehiculos_actuales += 1
                total_entradas += 1
                print('Entrada registrada correctamente')
                print(f'Espacios disponibles: {capacidad - vehiculos_actuales}')
            else:
                print('Estacionamiento sin espacio. No se permiten mas entradas')

        # Caso 2: Registrar salida y cobrar
        case '2':
            if vehiculos_actuales > 0:
                horas = int(input('Ingrese las horas facturadas: '))

                while horas <= 0:
                    print('Las horas deben ser mayores a cero')
                    horas = int(input('Ingrese las horas facturadas: '))

                monto = horas * tarifa
                total_ingresos += monto
                vehiculos_actuales -= 1
                total_salidas += 1

                print(f'Monto a pagar: ₡{monto}')
                print('Salida registrada correctamente')
            else:
                print('No hay vehiculos para registrar una salida')

        # Caso 3: Consultar ocupacion
        case '3':
            print(f'Vehiculos estacionados: {vehiculos_actuales}')
            print(f'Espacios disponibles: {capacidad - vehiculos_actuales}')

        # Caso 4: Consultar recaudacion
        case '4':
            print(f'Total recaudado: ₡{total_ingresos}')
            print(f'Total de vehiculos que han salido: {total_salidas}')

        # Caso 5: Salir
        case '5':
            print('\n--- RESUMEN FINAL ---')
            print(f'Vehiculos estacionados: {vehiculos_actuales}')
            print(f'Total de salidas: {total_salidas}')
            print(f'Total recaudado: ₡{total_ingresos}')
            print('Finalizando el programa')
            break

        case _:
            print('Opcion no valida')
