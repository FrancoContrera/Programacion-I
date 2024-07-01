array = [1,4,3,5,2]
for i in range(0, len(array)-1):
    print(f"{i}:")
    for j in range(i + 1, len(array)):
        #print(f"\t{j}")
        if array[i] > array[j]:
            auxiliar = array[i]
            array[i] = array[j]
            array[j] = auxiliar

print(array)