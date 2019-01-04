def Lectura_Archivo():
    arch = open("alumnos.txt", "r")
    linea = arch.readline().strip()
    while linea != "":
        partes = linea.split(",")
        nombre = partes[0]
        sexo = partes[1]
        alianza = partes[2]
        puntaje = int(partes[3])
        print(nombre)
        linea = arch.readline().strip()

def buscar_menor(lista):
    menor = 99
    for i in range(len(lista)):
        if lista[i] < menor:
            menor = lista[i]
    print(menor)
"""-------------------------------------------------------------"""
lista = [10,4,5,1,0,7]
buscar_menor(lista)


