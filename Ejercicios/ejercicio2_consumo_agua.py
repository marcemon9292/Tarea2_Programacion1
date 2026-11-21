# Ejercicio 2 - Registro semanal de consumo de agua (ejercicio2_consumo_agua.py/version 1)
# Curso: SOFT-01 - Principios de Programación I
# Autor: Marcela Otárola
# Fecha: 09/11/2026
# Descripción: Programa que registra el consumo de agua durante siete dias
# y calcula el total, promedio, consumo mayor y dias que superan 150 litros.

print ('¨Registro semanal de consumos de agua')
#variables
total_consumo = 0 #acumulador que suma L por dia
mayor_consumo = 0 # consumo mas alto
dias_mayores_150 = 0 #contador de dias mas altos (de uno en uno)

# Registro diario
for dia in range (1,8): # numeros del 1 al 7
    consumo_dia = float(input(f'Ingrese el consumo de agua del dia {dia} en L')) 
# Validar que el consumo no sea negativo
    while consumo_dia < 0:     # el while necesita que la variable pueda cambiar para que el ciclo termine.
        print('El consumo no puede ser negativo')
        consumo_dia = float(input(f'Ingrese el consumo del dia {dia}: '))
# Acumular el consumo diario
    total_consumo += consumo_dia     # total_consumo = total_consumo + consumo_dia

# Cual es el consumo mas alto?
    if consumo_dia > mayor_consumo:
        mayor_consumo = consumo_dia
        # Contar los dias con consumo mayor a 150 litros
    if consumo_dia > 150:
        dias_mayores_150 += 1

# Resultados

print(f'Consumo total semanal: {total_consumo} litros')

print(f'Mayor consumo diario: {mayor_consumo} litros')

print(f'Dias con consumo mayor a 150 litros: {dias_mayores_150}')

promedio = total_consumo / 7
print(f'Promedio diario: {promedio} litros')