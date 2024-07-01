def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> int | None:
    for i in range(reintentos):
        try:
            numero = int(input(mensaje))
            if minimo <= numero <= maximo:
                return numero
            else:
                print(mensaje_error)
        except ValueError:
            print("Error, ingrese un número válido.")

    print("Número de reintentos agotado.")
    return None

#numero_solicitado = get_int("Ingrese un numero: ", "Error, Reingrese nuevamente: ", 0, 100, 3)


#print(f"el numero solicitado es: {numero_solicitado}")

#edad = get_int("Ingrese su edad: " 18, 30, 3) 

#legajo = get_int("Ingrese su legajo: ",0, 1000, 2000,3)

#nota = get_int("Ingrese una nota: ", 0, 1, 10,3)

def get_float(mensaje: str, mensaje_error: str, minimo: float, maximo: float, reintentos: int) -> float|None:
    """Toma un float

    Args:
        mensaje (str): Titulo
        mensaje_error (str): Mensaje de error
        minimo (float): Minimo a comparar
        maximo (float): Maximo a comparar
        reintentos (int): Cantidad de reintentos

    Returns:
        float|None: Retorna el float o None
    """
    un_float = input(mensaje)
    un_float = float(un_float)
    while un_float < minimo or un_float > maximo:
        un_float = input("Reingrese nuevamente, tiene hasta 3 reintentos: ")
        un_float = float(un_float)

        reintentos -= 1
        if reintentos == 0:
            return None

    return un_float

#altura = get_float("Ingrese su altura (entre 1.50CM y 1.95CM): ",0, 1.50, 1.95 ,3)

def get_string(longitud: int, mensaje: str) -> str|None:
    """Toma una cadena y valida que sea de X caracteres

    Args:
        longitud (int): Numero de caracteres

    Returns:
        str|None: Retorna el numero de caracteres o None
    """
    cadena = input(mensaje)

    if len(cadena) == longitud:
        return cadena
    else:
        return None
    
#mensaje = "Ingrese una cadena de 6 caracteres: "
#longitud_deseada = 6
#cadena_valida = get_string(longitud_deseada, mensaje)
#if cadena_valida:
#    print("La cadena ingresada es:", cadena_valida)
#else:
#    print("No se ingresó una cadena válida.")

def sumar_naturales(numero: int) -> int:
    """Toma un numero natural y los sumas con sus anteriores

    Args:
        numero (int): El numero

    Returns:
        int: La suma de 5 + 4 + 3 + 2 + 1
    """
    if numero == 0:
        numero = 0
    else:
        numero += sumar_naturales(numero - 1)

    return numero

#numero = sumar_naturales(5)

#print(f"La suma de los primeros 5 naturales es: {numero}")

def calcular_potencia (numero_de_base: int, exponente : int) -> int:
    """Toma un numero y calcula la potencia

    Args:
        numero_de_base (int): Numero requerido
        exponente (int): Numero al que se va a elevar

    Returns:
        int: Resultado de la potencia
    """
    if exponente == 0:
        resultado = 1
    else:
        resultado = numero_de_base * calcular_potencia(numero_de_base, exponente - 1)

    return resultado

#base = input("Ingrese el numero de base: ")
#base = int(base)

#exponente = input("Ingrese su exponente: ")
#exponente = int(exponente)

#resultado = calcular_potencia(base, exponente)

#print(f"El resultado del exponente es: {resultado}")

def sumar_digitos (numero: int) -> int:
    """Toma un numero y suma sus digitos

    Args:
        numero (int): Numeros indicados

    Returns:
        int: La suma de esos numeros que se indican
    """
    if numero == 0:
        resultado = 0
    else:
        resultado = numero % 10 + sumar_digitos(numero // 10)

    return resultado

#resultado = sumar_digitos(123)

#print(f"La suma de los digitos es: {resultado}")

def calcular_fibonacci(numero: int, fibonacci_1: int = 0, fibonacci_2: int = 1) -> int:
    """
    Calcula el número de Fibonacci para un número dado utilizando recursión.

    Args:
        numero (int): El número para el cual se calculará el número de Fibonacci.
        fibonacci_1 (int): Valor inicial para el primer número de Fibonacci, al principio es 0
        fibonacci_2 (int): Valor inicial para el segundo número de Fibonacci, al principio es 1

    Returns:
        int: El numero de Fibonacci correspondiente al número dado.
    """
    if numero == 0:
        resultado = fibonacci_1
    elif numero == 1:
        resultado = fibonacci_2
    else:
        resultado = calcular_fibonacci(numero - 1, fibonacci_2, fibonacci_1 + fibonacci_2)

    return resultado

#numero = get_int("Seleccione un número: ", "Error", 0, 100, 3)
#resultado = calcular_fibonacci(numero)
#print(f"El número de Fibonacci de {numero} es {resultado}")






    






    




