import math

def calcularAngulo(lado_1, lado_2):
    angulo = math.atan(lado_2/lado_1)*(180/math.pi)
    return angulo

def calcularLadoTriangulo(puntoX1, puntoY1, puntoX2, puntoY2):
    lado = ((puntoX2 - puntoX1) ** 2 + (puntoY2 - puntoY1) ** 2) ** 0.5
    return lado

def calcularPerimetro(lado_A, lado_B, lado_C):
    perimetro = lado_A + lado_B + lado_C
    return perimetro



puntoX1 = float(input("Ingrese el punto x1: "))
puntoY1 = float(input("Ingrese el punto y1: "))

puntoX2 = float(input("Ingrese el punto x2: "))
puntoY2 = float(input("Ingrese el punto y2: "))

puntoX3 = float(input("Ingrese el punto x3: "))
puntoY3 = float(input("Ingrese el punto y3: "))

lado_A = calcularLadoTriangulo(puntoX1,puntoY1,puntoX2,puntoY2)
lado_B = calcularLadoTriangulo(puntoX2,puntoY2,puntoX3,puntoY3)
lado_C = calcularLadoTriangulo(puntoX3,puntoY3,puntoX1,puntoY1)

#isosceles
if lado_A == lado_B and lado_B == lado_C:
    print("equilatero")
elif lado_A == lado_B or lado_B == lado_C or lado_C==lado_A:
    print("Isosceles")
else:
    print("escaleno")

perimetro_obtenido = calcularPerimetro(lado_A, lado_B, lado_C)
anguloAB = calcularAngulo(lado_B, lado_A)
anguloAC = calcularAngulo(lado_A, lado_C)
anguloCB = calcularAngulo(lado_C, lado_B)

print(anguloAB)
print(anguloAC)
print(anguloCB)