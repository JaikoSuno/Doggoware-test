arch = open("helados.txt", "r")
linea = arch.readline().strip()
lugar_menor_vendedores = 999999
nombre_lugar_menor_vendedores = ""

lugar_mayor_vendedores = -1
nombre_lugar_mayor_vendedores = ""

sumador_cant_helados = 0

vendedor_mayor_helados = -1
nombre_vendedor_mayor_helados = ""

sumador_cant_helados_Plaza_Colon = 0
while linea != "": #LUGAR CON LOS VENDEDORES
    partes = linea.split(",")
    lugar_venta = partes[0]
    cant_vendedores = int(partes[1])

    if lugar_venta == "Plaza Colon":
        cant_vendedores_plaza_colon = cant_vendedores

    if cant_vendedores < lugar_menor_vendedores:
        lugar_menor_vendedores = cant_vendedores
        nombre_lugar_menor_vendedores = lugar_venta

    if cant_vendedores > lugar_mayor_vendedores:
        lugar_mayor_vendedores = cant_vendedores
        nombre_lugar_mayor_vendedores = lugar_venta

    for i in range(cant_vendedores): #LOS VENDEDORES
        linea = arch.readline().strip()
        partes = linea.split(",")
        nombre_vendedor = partes[0]
        cant_helados_vendidos = partes[1]
        sumador_cant_helados += cant_helados_vendidos
        if lugar_venta == "Plaza Colon":
            sumador_cant_helados_Plaza_Colon += cant_helados_vendidos

        if cant_helados_vendidos > vendedor_mayor_helados:
            vendedor_mayor_helados = cant_helados_vendidos
            nombre_vendedor_mayor_helados = nombre_vendedor


    linea = arch.readline().strip()

print(nombre_lugar_menor_vendedores)
print(nombre_lugar_mayor_vendedores)
print(sumador_cant_helados)
print(nombre_vendedor_mayor_helados)
print(sumador_cant_helados_Plaza_Colon/cant_vendedores_plaza_colon)