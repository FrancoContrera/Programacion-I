import random

def generar_legajos():
    """Genera una lista de legajos aleatorios

    Returns:
        _type_: Una lista de legajos aleatorios
    """
    legajos = [str(i) for i in range(100, 1600, 100)]
    random.shuffle(legajos)
    return legajos

def crear_matriz_legajos():
    """Crea una matriz de legajos

    Returns:
        _type_: Una matriz de legajos
    """
    legajos = generar_legajos()
    matriz_legajos = [[legajos[i], f"Chofer {i}"] for i in range(len(legajos))]
    return matriz_legajos

matriz_legajos = crear_matriz_legajos()

recaudaciones = []

def legajo_existe(legajo):
    """Verifica si un legajo existe en la lista de legajos

    Args:
        legajo (_type_): Lista de legajos

    Returns:
        _type_: Retorna True si el legajo existe y False si no existe
    """
    for legajo_chofer in matriz_legajos:
        if legajo_chofer[0] == legajo:
            print(f"El chofer con legajo {legajo} existe, su nombre es: {legajo_chofer[1]}")
            return True
    print(f"El chofer con legajo {legajo} no existe.")
    return False

def cargar_recaudaciones():
    """Carga las recaudaciones"""

    global recaudaciones
    legajo = input("Ingrese su legajo para identificarse: ")
    if legajo_existe(legajo):
        linea = input("Ingrese el nombre de la línea: ")
        colectivo = input("Ingrese el nombre del colectivo: ")
        monto = int(input("Ingrese el monto recaudado: "))
        nueva_recaudacion = {"legajo": legajo, "linea": linea, "coche": colectivo, "monto": monto}
        recaudaciones = recaudaciones + [nueva_recaudacion]

        print("Recaudación registrada exitosamente.")

def mostrar_recaudaciones_coches_lineas():
    """Muestra las recaudaciones por línea y colectivo"""
    recaudaciones_agrupadas = {}
    for recaudacion in recaudaciones:
        clave = (recaudacion['linea'], recaudacion['coche'])
        if clave not in recaudaciones_agrupadas:
            recaudaciones_agrupadas[clave] = 0
        recaudaciones_agrupadas[clave] += recaudacion['monto']
    
    for clave in recaudaciones_agrupadas:
        monto = recaudaciones_agrupadas[clave]
        linea, coche = clave
        print(f"La {linea} y el {coche} obtuvieron una recaudación de: {monto}$")

def calcular_recaudacion_por_linea(linea):
    """Calcula la recaudación por línea"""
    recaudacion_linea = 0
    for recaudacion in recaudaciones:
        if recaudacion['linea'] == linea:
            recaudacion_linea += recaudacion['monto']
    return recaudacion_linea

def calcular_recaudacion_por_coche(colectivo):
    """Calcula la recaudación por coche"""
    recaudacion_colectivo = 0
    for recaudacion in recaudaciones:
        if recaudacion['coche'] == colectivo:
            recaudacion_colectivo += recaudacion['monto']
    return recaudacion_colectivo

def mostrar_recaudacion_total():
    """Muestra la recaudación total"""
    recaudacion_total = 0
    for i in range(len(recaudaciones)):
        recaudacion_total += recaudaciones[i]['monto']
    return recaudacion_total