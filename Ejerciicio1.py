nivelEducacional = input("ingrese el nivel educacional: ")
sueldo_bruto = int(input("ingrese el sueldo bruto: "))
ciudad_origen = input("Ingrese ciudad de origen: ")
cant_Hijos = int(input("Ingrese la cantidad de hijos"))

bono = 0

if nivelEducacional == "profesional":
    impuesto = sueldo_bruto*0.2
else:
    impuesto = sueldo_bruto*0.1

if ciudad_origen == "Santiago":
    impuesto = impuesto - impuesto*0.1
elif ciudad_origen == "Antofagasta":
    impuesto = impuesto
else:
    impuesto = impuesto - impuesto*0.05

if nivelEducacional == "tecnico":
    bono = (bono + sueldo_bruto*0.02)*cant_Hijos
else:
    bono = (bono + sueldo_bruto*0.01)*cant_Hijos

sueldo_bruto_final = sueldo_bruto - impuesto + bono
print(sueldo_bruto_final)
print(impuesto)