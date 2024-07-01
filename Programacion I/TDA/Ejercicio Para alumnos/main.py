from Grafico import *
from os import *

def inicio_programa():
    system("cls")
    while True:
        opcion = int(input("1. Seleccionar figura y cargar valores\n2. Visualizar resultados\n3. Salir\nElija una opción: "))
        match opcion:
            case 1:
                system("cls")
                print("¿Qué tipo de figura desea representar?")
                que_figura = input("a. Círculo\nb. Rectángulo\nc. Triángulo\nd. Volver al menu anterior\nElija una opción: ")
                match que_figura:
                    case "a":
                        system("cls")
                        radio = int(input("Ingrese el valor del radio: "))
                        color = seleccionar_color("Elige un color: ")
                        figura = {"tipo": "Circulo", "color": color, "dimensiones": [radio], "posicion": [500,425]}
                    case "b":
                        system("cls")
                        base = int(input("Ingrese el valor del rectangulo (base): "))
                        altura = int(input("Ingrese el valor del rectangulo (altura): "))
                        color = seleccionar_color("Elige un color: ")
                        figura = {"tipo": "Rectangulo", "color": color, "dimensiones": [base, altura], "posicion": [500,425]}
                    case "c":
                        system("cls")
                        base = int(input("Ingrese el valor de la base del triangulo: "))
                        altura = int(input("Ingrese el valor de la altura del triangulo: "))
                        color = seleccionar_color("Elige un color: ")
                        figura = {"tipo": "Triangulo", "color": color, "dimensiones": [base, altura], "posicion": [500,425]}
                    case "d":
                        continue
                    case _:
                        print("Opccion invalida")
            case 2:
                graficar(figura)
            case 3:
                print("Gracias por usar nuestro programa")
                break 
            
        system("cls")   

inicio_programa()