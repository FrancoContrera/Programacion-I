import time

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

def particionar(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            swap(array, i, j)
    swap(array, i + 1, high)
    return i + 1

def quick_sort_iterativo(array):
    procesos = 0  
    limites = [(0, len(array) - 1)]  
    while limites:
        procesos += 1
        low, high = limites[0] 
        limites = limites[1:]
        while low < high:
            pi = particionar(array, low, high)
            if pi - low < high - pi:
                limites = [(low, pi - 1)] + limites 
                low = pi + 1
            else:
                limites = [(pi + 1, high)] + limites 
                high = pi - 1
    return procesos

vector = [5,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,1,9,7,3,1,9,7,3,1,9,7,
          3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,
          7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,
          7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,
          1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,
          1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,
          1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3]

start = time.time()
procesos = quick_sort_iterativo(vector)
end = time.time()

print("Número de procesos:", procesos)
print("Tiempo:", (end - start) * 1000, "milisegundos")
print(vector)