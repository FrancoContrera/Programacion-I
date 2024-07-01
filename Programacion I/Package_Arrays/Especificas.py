from Package_Arrays.Package_Arrays.Array_generales import *

def pedir_ingreso_numeros(lista):
    """Pide al usuario que ingrese una lista de enteros y los devuelve

    Returns:
        _type_: Devuelve una lista de enteros
    """
    for get_int in range(len(lista)): 
        lista[get_int] = get_int
    return lista 

#lista = pedir_ingreso_numeros([0, 0, 0, 0, 0])
#print(f"La lista es: {lista}")

def mostrar_cantidad_numeros_positivos_negativos(lista):
    """Muestra la cantidad de positivos y negativos

    Args:
        lista (_type_): Recibe una lista de numeros positivos y negativos

    Returns:
        _type_: Devuelve la cantidad de positivos y negativos
    """
    cantidad_positivos = 0
    cantidad_negativos = 0

    for get_int in range(len(lista)):
        if lista[get_int] > 0:
            cantidad_positivos += 1
            resultado_positivos = cantidad_positivos
        else:
            cantidad_negativos += 1
            resultado_negativos = cantidad_negativos

    return resultado_positivos, resultado_negativos

#cantidad_numeros = (mostrar_cantidad_numeros_positivos_negativos([-10 , 10, 20]))
#print(f"La cantidad de positivos es {cantidad_numeros[0]} y la de negativos es {cantidad_numeros[1]}")

def sumar_pares(lista):
    """Recibe una lista de numeros, verifica que sean pares y los suma

    Args:
        lista (_type_): Suma en caso de que sean pares

    Returns:
        _type_: Devuelve la suma de los pares
    """
    sumar_pares = 0

    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            sumar_pares += lista[i]
    
    return sumar_pares

#resultado = (sumar_pares([2,3,6,4]))
#print(f"La suma de los pares de la lista es: {resultado}")

def buscar_maximo_impares(lista):
    """Recibe una lista de numeros, verifica que sean impares e informa cual es el mayor de ellos

    Args:
        lista (_type_): Recibe una lista de numeros impares

    Returns:
        _type_: Devuelve el mayor de los impares
    """
    maximo_impares = 0

    for i in range(len(lista)):
        if lista[i] % 2 == 1 and (maximo_impares == 0 or lista[i] > maximo_impares):
            maximo_impares = lista[i]
    
    return maximo_impares

#resultado = (buscar_maximo_impares([2,3,6,9]))
#print(f"El maximo impar de la lista es: {resultado}")

def listar_numeros(lista):
    """Recibe una serie de numeros y los lista

    Args:
        lista (_type_): Recibe una lista de enteros
    """
    
    for i in range(len(lista)):
        if lista[i] > 0:
            print(f"Los numeros de la lista son {lista[i]}")

    return lista

#numeros_ingresados = listar_numeros([5, 7, 8, 6, 5])
#print(f"La lista es: {numeros_ingresados}")

def listar_pares(lista):
    """Recibe una lista de enteros,verifica que sean pares y los pone en una lista

    Args:
        lista (_type_): Recibe una lista de numeros pares

    Returns:
        _type_: Devuelve una lista de pares
    """

    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            print(f"Los pares de la lista son: {lista[i]}")
    return lista
    
#list_pares = listar_pares([2, 4, 6, 8, 10])
#print(f"La lista de pares es: {list_pares}")

def listar_posisciones_impares(lista):
    """Recibe una lista de impares y lista las posiciones de los numeros impares

    Args:
        lista (_type_): Recibe una lista de numeros impares

    Returns:
        _type_: Devuelve las posiciones de los impares
    """

    for i in range(len(lista)):
        if lista[i] % 2 == 1:
            print(f"Las posiciones de los impares de la lista son: {i+1}")

    return lista

#list_impares = listar_posisciones_impares([2, 3, 4, 7, 9])
#print(f"La lista de impares es: {list_impares}")
            
        
   




