from os import system
from Package_Arrays.Package_Arrays.Especificas import *
from Package_Arrays.Package_Arrays.Array_generales import *
from Package_funciones.input import *

bandera_seguir = True
bandera_numeros_ingresados = False
lista = []

while bandera_seguir:
    opcion = int(input("Que desea hacer: \n"`
                       "1. Ingrese numeros \n"
                       "2. Mostrar la cantidad de números positivos y negativos \n"
                       "3. Mostrar la sumatoria de los números pares \n"
                       "4. Informar el mayor de los números impares \n"
                       "5. Listar todos los números ingresados \n"
                       "6. Listar todos los números pares \n"
                       "7. Listar los números de las posiciones impares \n"
                       "8. Salir \n"))

    match opcion:
        case 1:
            for i in range(3):
                numero = get_int("Ingrese un numero entre -1000 y 1000: ",
                                 "Error, Reingrese nuevamente: ", -1000, 1000, 3)
                # Asignar directamente el número a la lista en la posición i
                lista[i] = numero
                bandera_numeros_ingresados = True
        case 2:
            if bandera_numeros_ingresados:
                cantidad_numeros = mostrar_cantidad_numeros_positivos_negativos(lista)
                print(f"{cantidad_numeros} Numeros Positivos/Negativos")
            else:
                print("Primero ingrese números.")
        case 3:
            if bandera_numeros_ingresados:
                sumar_pares = sumar_pares(lista)
                print(f"La suma de los pares es: {sumar_pares}")
            else:
                print("Primero ingrese números.")
        case 4:
            if bandera_numeros_ingresados:
                maximo_impares = buscar_maximo_impares(lista)
                print(f"El mayor de los impares es: {maximo_impares}")
            else:
                print("Primero ingrese números.")
        case 5:
            if bandera_numeros_ingresados:
                print(f"Los valores ingresados son: {lista}")
            else:
                print("Primero ingrese números.")
        case 6:
            if bandera_numeros_ingresados:
                print(f"Los valores pares son: {listar_pares(lista)}")
            else:
                print("Primero ingrese números.")
        case 7:
            if bandera_numeros_ingresados:
                print(f"Los valores impares son: {listar_posisciones_impares(lista)}")
            else:
                print("Primero ingrese números.")
        case 8:
            seguir = input("Desea seguir (SI/NO): ")
            if seguir.upper() == "NO":
                print("Saliendo del programa")
                bandera_seguir = False

    system("pause")
    system("cls")