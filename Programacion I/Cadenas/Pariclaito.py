vector = [3,8,1,4,7] #Se define el vector inicial
axuliar = 0 #Se agrega una variable auxiliar en 0

for i in range (1, len(vector)): # Se recorre el vectorm hasta el penúltimo
    for j in range(i, len(vector)-1):
        if vector[j] < vector[j+1]: #Se compara si el elemento actual es menor que el anterior
            axuliar = vector[j] #Ahora se intercambian entre los elementos
            vector[j] = vector[j+1]
            vector[j+1] = axuliar
print(vector)
