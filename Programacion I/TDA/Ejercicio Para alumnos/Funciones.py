from math import *

#region Calculos

def calcular_area_rectangulo(base, altura):
    calculo = base * altura
    return calculo

def calcular_perimetro_rectangulo(base, altura):
    calculo = 2* (base + altura)
    return calculo


def calcular_area_circulo(radio):
    calculo = pi * (radio**2)
    return calculo


def calcular_perimetro_circulo(radio):
    calculo = 2 * pi * radio
    return calculo

def calcular_area_triangulo_rectangulo(base, altura):
    calculo = base * altura / 2
    return calculo

def calcular_perimetro_triangulo_rectangulo(base, altura):
    hipotenusa = sqrt(base**2 + altura**2)
    calculo = base + altura + hipotenusa
    return calculo


#endregion

    
