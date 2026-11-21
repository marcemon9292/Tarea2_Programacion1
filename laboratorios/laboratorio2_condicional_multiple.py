
# Laboratorio 2 - Condicional multiple
# Curso: SOFT-01 - Principios de Programacion I
# Descripcion: Calcular el descuento de una compra segun el monto

def determinar_descuento(monto):
    # Definir el descuento segun el monto de la compra
    if monto < 5000:
        descuento = 0
    elif 5000 <= monto < 10000:
        descuento = 0.05
    elif 10000 <= monto < 25000:
        descuento = 0.11
    elif 25000 <= monto < 50000:
        descuento = 0.18
    else:
        descuento = 0.25

    # Calcular cuanto se descuenta
    monto_descuento = monto * descuento

    # Restar el descuento al monto original
    total = monto - monto_descuento

    print(f'El monto final es de {total}')


# Solicitar el monto de la compra
monto_compra = float(input('Ingrese el monto de la compra: '))

determinar_descuento(monto_compra)
