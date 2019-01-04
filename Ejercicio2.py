cant_facturas = int(input("Ingrese la cantidad de facturas: "))


mayor_venta = -1
sumador_total_neto = 0
total_impuesto_pagado = 0
for x in range(cant_facturas): #cada factura
    sumador_neto = 0
    cant_items = int(input("Ingrese la cantidad de items: "))
    for i in range(cant_items): #cada item
        cant_productos = int(input("Ingrese la cantidad de productos: "))
        for i in range(cant_productos): #cada producto
            monto_neto = int(input("Ingrese la cantidad de productos: "))
            sumador_neto = sumador_neto + monto_neto
            sumador_total_neto += monto_neto
    total_impuesto = sumador_neto*0.19
    total_impuesto_pagado += total_impuesto

    if mayor_venta < sumador_neto:
        mayor_venta = sumador_neto
        numero_factura = x + 1

    print(sumador_neto)
    print(total_impuesto)
print(sumador_neto/cant_facturas)
print(total_impuesto_pagado)
print(numero_factura)


