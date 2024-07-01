def detectar_vocales (cad):
    """Recibe una cadena y detecta cuantas vocales hay

    Args:
        cad (_type_): Recibe una cadena
    
    Returns:
        _type_: Devuelve cuantas vocales hay
    """

    vocales = 'aeiouAEIOU'
    cantidad_vocales = {'a':0,'e':0,'i':0,'o':0,'u':0,'A':0,'E':0,'I':0,'O':0,'U':0} 

    for i in range(len(cad)):
        if cad[i] in vocales:
            cantidad_vocales[cad[i]] += 1

    for i in range(len(vocales)):
        vocal = vocales[i]
        if cantidad_vocales[vocal] > 0:
            print(f"La vocal {vocal} aparece {cantidad_vocales[vocal]} veces")


#detectar_vocales("aaaaaeeeeeeiiooouuuu")

def devolver_indice (cad, caracter):
    """Devuelve el indice en el que se encuentra la primera incidencia de un caracter

    Args:
        cad (_type_): Recibe una cadena y un caracter
    
    Returns:
        _type_: Devuelve el índice en el que se encuentre la primera incidencia de dicho caracter, o -1 en caso de que no esté.
    """

    for i in range(len(cad)):
        if cad[i] == caracter:
            print(f"El caracter {caracter} aparece en la posición {i}")
            return i

    print(f"El caracter {caracter} no aparece en la cadena")
    return -1

#devolver_indice("holajiu", "i")

def es_palindromo(cadena):
    cadena_reves = list(cadena[::-1])
    if list(cadena) == cadena_reves:   
        cadena = print("Es palindromo")
    else:
        cadena = print("No es palindromo")

    return cadena
        
#es_palindromo("ana")

def suprimir_caracteres(cadena):
    """Recibe una cadena y suprime los caracteres repetidos en caso de haberolos

    Args:
        cadena (_type_): Recibe una cadena

    Returns:
        _type_: Retorna la cadena suprimiendo sus repetidos
    """
    resultado =  ""
    for i in range(len(cadena)):
        suprimir = True
        for j in range(len(resultado)):
            if cadena[i] == resultado[j]:
                suprimir = False
                break

        if suprimir:
            resultado += cadena[i]

    return resultado

cadena = "hoooola"

#print(suprimir_caracteres(cadena))

def suprimir_vocales (cadena):
    """Recibe una cadena y suprime las vocales

    Args:
        cad (_type_): Recibe una cadena
    
    Returns:
        _type_: Devuelve la cadena suprimiendo las vocales
    """

    vocales = 'aeiouAEIOU'
    cantidad_vocales = {'a':0,'e':0,'i':0,'o':0,'u':0,'A':0,'E':0,'I':0,'O':0,'U':0} 
    resultado = ""

    for i in range(len(cadena)):
        if cadena[i] in vocales:
            cantidad_vocales[cadena[i]] += 1
        else:
            resultado += cadena[i]
    for vocal in cantidad_vocales:
        if cantidad_vocales[vocal] > 0:
            print(f"Se suprime la vocal {vocal}")

    return resultado

cadena = "hoooola"
print(suprimir_vocales(cadena))

def contador_subcadenas(cadena,subcadena):
    """Recibe una cadena y cuenta cuantas veces aparece una subcadena

    Args:
        cadena (_type_): Recibe una cadena
        subcadena (_type_): Recibe una subcadena
    
    Returns:
        _type_: Devuelve la cantidad de veces que aparece la subcadena
    """
    contador_subcadena = 0
    for i in range(len(cadena)):
        if cadena[i:i+len(subcadena)] == subcadena:
            contador_subcadena += 1

    return contador_subcadena

print(contador_subcadenas("mamelucomameluco","mame"))





