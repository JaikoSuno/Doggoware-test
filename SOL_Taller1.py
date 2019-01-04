cant_archivos_leidos = 0
cantidad_steam = 0
cantidad_fisico = 0
cantidad_total_juegos = 0

unidades_vendidas_steam = 0
unidades_vendidas_fisico = 0

mayor_compra_pais = -1
nombre_mayor_compra_pais = ""

menor_compra_juego = 999999
nombre_menor_compra_juego = ""

nombre_archivo = input("Ingrese el nombre del archivo: ")
while nombre_archivo != "CIERRE":
    try:
        arch = open(nombre_archivo, "r")
        linea = arch.readline().strip()
        cant_archivos_leidos += 1
        while linea != "":
            partes = linea.split(";")
            pais = partes[0]
            juego = partes[1]
            unidades_vendidas = int(partes[2])
            valor_juego = float(partes[3])
            plataforma = partes[4]

            if plataforma == "STEAM":
                unidades_vendidas_steam += unidades_vendidas
                cantidad_steam += 1
            else:
                unidades_vendidas_fisico += unidades_vendidas
                cantidad_fisico += 1

            if unidades_vendidas > mayor_compra_pais:
                mayor_compra_pais = unidades_vendidas
                nombre_mayor_compra_pais = pais

            if unidades_vendidas < menor_compra_juego:
                menor_compra_juego = unidades_vendidas
                nombre_menor_compra_juego = juego


            cantidad_total_juegos += 1

            linea = arch.readline().strip()
    except FileNotFoundError:
        print("[!] Error: El archivo no existe")
    except:
        print("[!] Error desconocido")
    nombre_archivo = input("Ingrese el nombre del archivo: ")

if cantidad_total_juegos != 0:
    print("Promedio de juegos vendidos en Steam:", unidades_vendidas_steam/cantidad_steam)
    print("Promedio de juegos vendidos en Fisico:", unidades_vendidas_fisico/cantidad_fisico)
    print("Pais con mayor venta en una transaccion:", nombre_mayor_compra_pais)
    print("Juegos con menor venta en una transaccion:", nombre_menor_compra_juego)
    sumatotal=(cantidad_fisico+cantidad_steam)
    print("Porcentaje de ventas Steam:", cantidad_steam*100/cantidad_total_juegos)
    print("Porcentaje de ventas Fisico:", cantidad_fisico*100/cantidad_total_juegos)
else:
    print("[!] No se tiene informacion sufieciente")