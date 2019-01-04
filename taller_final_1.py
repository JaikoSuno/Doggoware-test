#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 12:43:15 2018

@author: paulinedemanet
"""

Contador = 0
Fisico = 0
Steam = 0

k = 0
h = 0


mayorM = -999
menorm = 9999999
cant_arch = 0
nombre_archivo = input("Ingrese nombre: ")
while nombre_archivo != "CIERRE":

    try:
        arch = open(nombre_archivo, "r")
        cant_arch += 1
        lin = arch.readline().strip()
        while lin != "":
            parte = lin.split(";")
            plataforma = parte[0]

            if plataforma == "Físico":
                Fisico = Fisico + cant
                k += 1

            if plataforma == "Steam":
                Steam = Steam + cant
                h += 1

            if mayor > mayorM:
                mayorM = mayor
                paismayorM = paismayor

            if menor < menorm:
                menorm = menor
                juegomenorm = juegomenor
        lin = arch.readline().strip()
    nombre_archivo = input("Ingrese nombre: ")

            
PromFisico = float(Fisico)/(k+h)           
PromSteam = float(Steam)/(h+k)
porcF = float(Fisico)/(Steam+Fisico)
porcS = float(Steam)/(Steam+Fisico)

print ("Cantidad de archivos leidos:", Contador)
cierre = ""
cierre = open(cierre.txt,"w")
cierre.write("promedio juego vendidos por fisico es",PromFisico,"\n")
cierre.write("promedio juego vendidos por steam es",PromSteam,"\n")
cierre.write("pais con mas ventas es",paismayorM,"\n")
cierre.write("el juego menos vendido es",juegomenorm,"\n")
cierre.write("el porcentaje de juegos vendidos por steam es",porcS,"% \n")
cierre.write("el porcentaje de juegos vendidos en fisico es",porcF,"% \n")
cierre.write("el total de archivos leidos esta semana es",Contador,"\n")
cierre.close()
