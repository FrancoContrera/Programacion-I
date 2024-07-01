filas1 = int(input("Ingresar el numero de filas de la primera Matriz: "))
columnas1 = int(input("Ingresar el numero de columnas de la primera Matriz: "))

filas2 = int(input("Ingresar el numero de filas de la segunda Matriz: "))
columnas2 = int(input("Ingresar el numero de columnas de la segunda Matriz: "))

if columnas1 != filas2:
    print("Las matrices no se pueden multiplicar por que el numero de columnas de la primera Matriz es diferente al numero de filas de la segunda Matriz")
    exit(print("El programa se cerrara por datos erroneos"))

print("Ingresar los elementos de la primera Matriz: ")

matriz1 = []

for i in range(filas1):
    fila = []
    for j in range(columnas1):
        elemento = int(input(f"Ingresar el elemento [{i}][{j}]: "))
        fila += [elemento]
    matriz1 += [fila]

print("Ingresar los elementos de la segunda matriz: ")

matriz2 = []
for i in range(filas2):
    fila = []
    for j in range(columnas2):
        elemento = int(input(f"Ingresar el elemento [{i}][{j}]: "))
        fila += [elemento]
    matriz2 += [fila]

#multiplicacion
resultado = []
for i in range(filas1): 
    resultado_fila = []
    for j in range(columnas2):
        suma = 0
        for k in range(filas2):
            suma += matriz1[i][k] * matriz2[k][j]
        resultado_fila += [suma]
    resultado += [resultado_fila]

print("El resultdo de la multiplicacion de las matrices es: ")
for i in range(len(matriz1)): #devuelve longitud de la primera matriz
    for j in range(len(matriz2[0])): 
        print(resultado[i][j], end=" ") #imprime la matriz
    print()




