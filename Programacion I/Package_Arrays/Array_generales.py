def calcular_promedio_enteros(lista: list) -> float:
    """Suma una lista de enteros y da su promedio

    Args:
        lista (list): Recibe una lista de numeros enteros

    Returns:
        float: El promedio de estos enteros
    """
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]
    return suma / len(lista)

# lista = [50 , 25]
# print(f"El promedio de los enteros en la lista: {lista} es {calcular_promedio_enteros(lista)}")

def calcular_promedio_positivos_enteros(lista: list) -> float | None:
    """Suma enteros solamente positivos y retorna su promedio

    Args:
        lista (list): Recibe enteros positivos

    Returns:
        float | None: El promedio de los enteros positivos
    """
    if type(lista) == list and len(lista) > 0:
        suma_positivos = 0
        cantidad_positivos = 0
        for i in range (len(lista)):
            if lista[i] > 0:
                suma_positivos += lista[i]
                cantidad_positivos += 1
        if cantidad_positivos > 0:
            resultado = suma_positivos / cantidad_positivos
        else:
            print("No hay números positivos en la lista.")
            resultado = None
    else:
        print("La entrada no es una lista válida o está vacía.")
        resultado = None
    return resultado
        
# lista = [50, -25]
# print(f"El promedio de números positivos en {lista} es: {calcular_promedio_positivos_enteros(lista)}")

def calcular_producto_enteros(lista: list) -> int:
    """Multiplica enteros y retorne el producto de todos los elementos de la lista que recibe como parámetro.

    Args:
        lista (list): Lista de enteros

    Returns:
        int: El producto de todos los elementos de la lista
    """
    producto = 1
    for i in range(len(lista)):
        producto *= lista[i]
    return producto

# lista = [40, 1 , 3]
# print(f"El producto de {lista} es: {calcular_producto_enteros(lista)}")


def buscar_maximos(lista:list) -> int | None:
    """calcula y retorna el maximo de los elementos de la lista

    Args:
        lista (list): 

    Returns:
        list:
    """
    bandera_maximo = True
    for i in range(len(lista)):
        if bandera_maximo == True or lista[i] > maximo:
            maximo = lista[i]
            bandera_maximo = False
    return maximo
# lista = [0, 1 , 2]
# print(f"El maximo de {lista} es: {buscar_maximos(lista)}")

def buscar_posicion_maximos(lista:list) -> int | None:
    """Detecta la posicion del valor maximo

    Args:
        lista (list): Los elementos de la lista

    Returns:
        int | None: La posicion del valor maximog
    """
    maximo = 0
    posicion_maximo = 0
    
    for i in range(len(lista)):
        if lista[i] > maximo:
            maximo = lista[i]
            posicion_maximo = i + 1
            
    return posicion_maximo

# lista = [1,5,4,3,55]
# print(f"La posicion del maximo de la lista: {lista} es la numero {buscar_posicion_maximos(lista)}")

def reemplazar_nombres(lista:list) -> list:
    """ Reemplaza un nombre determinado y luego retorna la cantidad total de reemplazos realizados

    Args:
        lista (list): Recibe una lista de nombres

    Returns:
        list: Retorna la cantidad de reemplazos
    """
    reemplazos = 0
    nombre = input("Ingrese el nombre que desea reemplazar: ")
    reemplazar = input("Ingrese el nuevo nombre: ")
    for i in range(len(lista)):
        if lista[i] == nombre:
            lista[i] = reemplazar
            reemplazos += 1
    return reemplazos

# lista = ["Fran", "Pedro", "Santi"]
# print(f"La cantidad de reemplazos es: {reemplazar_nombres(lista)} y la lista quedaria de esta manera: {lista}")







        
    