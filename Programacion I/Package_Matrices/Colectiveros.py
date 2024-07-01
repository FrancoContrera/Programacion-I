from os import system
from Especificas_Matrices import *

bandera_seguir = True

while bandera_seguir:
    opcion = int(input("""\
1. Identificarse para cargar recaudaciones                      
2. Mostrar la recaudación de todos los coches y líneas                       
3. Calcular y mostrar recaudación por línea                      
4. Calcular y mostrar recaudación por coche                      
5. Calcular y mostrar la recaudación total                      
6. Salir
"""))

    if opcion == 1:
        cargar_recaudaciones()
    elif opcion == 2:
        mostrar_recaudaciones_coches_lineas()
    elif opcion == 3:
        linea = input("Ingrese el nombre de su linea: ")
        print(f"La recaudación para la {linea} es: {calcular_recaudacion_por_linea(linea)}$")
    elif opcion == 4:
        colectivo = input("Ingrese el nombre del colectivo: ")
        print(f"La recaudación para el {colectivo} es de: {calcular_recaudacion_por_coche(colectivo)}$")
    elif opcion == 5:
        print(f"La recaudación total es: {mostrar_recaudacion_total()}$")
    elif opcion == 6:
        print("Saliendo del programa...")
        bandera_seguir = False
    else:
        print("Opción no válida.")

    system("pause")
    system("cls")