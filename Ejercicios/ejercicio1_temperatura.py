# Ejecicio 1 ~ Control de temperatura en camara experimental (ejercicio1_temperatura.py/version 1)
# Curso: SOFT-01 - Principios de Programación I
# Autor: Marcela Otárola
# Fecha: 09/11/2026
# Descripción: Programa que simula el calentamiento de una cámara experimental

print ('Control de temperatura en una camara experimental')
# Ingresar los datos
temperatura_inicial = float(input('Ingrese la temperratura inicial en Celsius: '))
temperatura_objetivo = float(input('Ingrese la temperatura objetivo en Celsius: '))
incremento = float(input('Ingrese el incremento de temperatura por cada ciclo: '))
# Inicializacion de las variables
temperatura_actual = temperatura_inicial
ciclos = 0
# Validar datos
if (temperatura_objetivo <= temperatura_inicial):
    print('Invalido: La temperatura objetivo debe ser mayor que la temperatua inicial.')
elif (incremento <= 0):
    print('Invalido: El incremento debe ser mayor a cero')
else:
    print ('Datos validados e iniciando el aumento de temperatura...')

# Simulación del aumento de temperatura
    while (temperatura_actual < temperatura_objetivo):
        temperatura_actual += incremento #temperatura_actual = temperatura_actual + incremento
        ciclos += 1 #contador. Cada vez que se ejecuta el ciclo, aumenta en una unidad.
        #variable numérica que se inicializa y se incrementa o decrementa en una cantidad fija para llevar el registro de repeticiones o eventos.
        print(f'Ciclo {ciclos}: Temperatura actual {temperatura_actual} grados Celsius') #f-string (incluir el valor de una variable directamente dentro de un texto.)

# Resultados finales
    print(f'Temperatura final alcanzada: {temperatura_actual} grados Celsius')
    print(f'Total de ciclos realizados: {ciclos}')



