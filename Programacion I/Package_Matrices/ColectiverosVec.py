import random
from os import system


legajos_choferes = [str(i) for i in range(100, 1600, 100)]
random.shuffle(legajos_choferes)

recaudaciones = []

def legajo_existe(legajo):
    """Verifica si un legajo existe en la lista de legajos

    Args:
        legajo (str): Legajo a verificar

    Returns:
        bool: True si el legajo existe, False si no existe
    """
    if legajo in legajos_choferes:
        print(f"El chofer con legajo {legajo} existe.")
        return True
    else:
        print(f"El chofer con legajo {legajo} no existe.")
        return False

def cargar_recaudaciones():
    """Carga las recaudaciones"""
    legajo = input("Ingrese su legajo para identificarse: ")
    global recaudaciones
    if legajo_existe(legajo):
        linea = input("Ingrese el nombre de la línea: ")
        colectivo = input("Ingrese el nombre del colectivo: ")
        monto = int(input("Ingrese el monto recaudado: "))
        nueva_recaudacion = [legajo, linea, colectivo, monto]
        recaudaciones = recaudaciones + [nueva_recaudacion]
        print("Recaudación registrada exitosamente.")

def mostrar_recaudaciones_coches_lineas():
    """Muestra las recaudaciones por línea y colectivo"""
    recaudaciones_agrupadas = {}
    for recaudacion in recaudaciones:
        clave = (recaudacion[1], recaudacion[2])
        recaudaciones_agrupadas[clave] = recaudaciones_agrupadas.get(clave, 0) + recaudacion[3]
    
    for clave, monto in recaudaciones_agrupadas.items():
        linea, coche = clave
        print(f"La {linea} y el {coche} obtuvieron una recaudación de: {monto}$")

def calcular_recaudacion_por_linea(linea):
    """Calcula la recaudación por línea"""
    recaudacion_linea = 0
    for recaudacion in recaudaciones:
        if recaudacion[1] == linea:
            recaudacion_linea += recaudacion[3]
    return recaudacion_linea

def calcular_recaudacion_por_coche(colectivo):
    """Calcula la recaudación por coche"""
    recaudacion_colectivo = 0
    for recaudacion in recaudaciones:
        if recaudacion[2] == colectivo:
            recaudacion_colectivo += recaudacion[3]
    return recaudacion_colectivo

def mostrar_recaudacion_total():
    """Muestra la recaudación total"""
    recaudacion_total = 0
    for recaudacion in recaudaciones:
        recaudacion_total += recaudacion[3]
    return recaudacion_total

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