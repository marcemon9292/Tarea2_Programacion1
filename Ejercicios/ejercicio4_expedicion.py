# Ejercicio 4 ~ Gestion de recursos de expedicion (ejercicio4_expedicion.py / Version 1)
# Curso: SOFT-01 - Principios de Programación I
# Autor: Marcela Otárola
# Fecha: 11/11/2026
# Descripción: Programa que controla el consumo diario de agua y comida durante una expedicion.

print('Sistema de gestion de recursos de expedicion')

# Recursos iniciales
agua_disponible = 150
comida_disponible = 100

# Contadores y acumuladores
dias_completados = 0 # Contador de días registrados.
total_agua_consumida = 0 # Acumulador del agua consumida.
total_comida_consumida = 0 # Acumulador de la comida consumida.

# Solicitar cantidad de jornadas
jornadas = int(input('Ingrese la cantidad de jornadas (1 a 30): '))

while jornadas < 1 or jornadas > 30:
    print('La cantidad de jornadas debe estar entre 1 y 30')
    jornadas = int(input('Ingrese la cantidad de jornadas (1 a 30): '))


# Registro diario de consumo
for dia in range(1, jornadas + 1): # Recorre la cantidad de jornadas ingresadas.
    print(f'\n--- Dia {dia} ---') # Muestra el número de la jornada actual.
    print(f'Agua disponible: {agua_disponible} litros')
    print(f'Comida disponible: {comida_disponible} unidades')

    # Solicitar consumo diario
    consumo_agua = float(input('Ingrese los litros de agua consumidos: '))

    # Validar consumo de agua
    while consumo_agua <= 0 or consumo_agua > agua_disponible:
        print('Consumo invalido. Debe ser mayor a cero y no superar el agua disponible')
        consumo_agua = float(input('Ingrese los litros de agua consumidos: '))

    consumo_comida = int(input('Ingrese las unidades de comida consumidas: '))

    # Validar consumo de comida
    while consumo_comida <= 0 or consumo_comida > comida_disponible:
        print('Consumo invalido. Debe ser mayor a cero y no superar la comida disponible')
        consumo_comida = int(input('Ingrese las unidades de comida consumidas: '))
  

    # Actualizar recursos disponibles
    agua_disponible -= consumo_agua
    comida_disponible -= consumo_comida

    print(f'Agua restante: {agua_disponible} litros')
    print(f'Comida restante: {comida_disponible} unidades')

    # Acumular consumo
    total_agua_consumida += consumo_agua
    total_comida_consumida += consumo_comida

    # Contar el dia registrado
    dias_completados += 1

    # Verificar si se agotaron los recursos
    if (agua_disponible == 0 or comida_disponible == 0) and dia < jornadas:
        print('La expedicion termina por agotamiento de recursos')
        break

# Calcular promedios diarios
promedio_agua = total_agua_consumida / dias_completados
promedio_comida = total_comida_consumida / dias_completados

# Mostrar resultados finales
print('\n--- RESUMEN DE LA EXPEDICION ---')
print(f'Dias completados: {dias_completados}')
print(f'Agua consumida: {total_agua_consumida} litros')
print(f'Comida consumida: {total_comida_consumida} unidades')
print(f'Promedio diario de agua: {promedio_agua:.2f} litros')  # Muestra un número decimal con dos cifras después del punto.
print(f'Promedio diario de comida: {promedio_comida:.2f} unidades')
print(f'Agua restante: {agua_disponible} litros')
print(f'Comida restante: {comida_disponible} unidades')

# Comprueba si se completaron todas las jornadas programadas.
if dias_completados == jornadas: # 	Comprueba si se completaron los 30 días.
    print('Estado: Expedicion completada')
else:
    print('Estado: Expedicion finalizada por agotamiento de recursos')