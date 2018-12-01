def readInput():
    value = input()
    array = input()
    array = array.split(" ")
    arrayNum = [int(elem) for elem in array]

    return arrayNum, int(value)

def binarySearch(array, value, start, end):
    mid = int((start + end - 1)/2)
    if (mid < start or mid > end or mid < 0 or start + end - 1 < 0):
        print("O elemento nao foi encontrado")
        return
    printArray(array, start, end, array[mid])

    if array[mid] == value:
        print("O elemento estah na posicao " + str(mid))
        return
    elif array[mid] < value:
        binarySearch(array, value, mid+1, end)
    elif array[mid] > value:
        binarySearch(array, value, start, mid)

def IsArrayOrdered(array):
    array2 = sorted(array)
    for i in range(len(array)):
        if array2[i] != array[i]:
            return False
    return True

def printArray(array, start, end, value):
    for i in range(0,end):
        if i < start:
            print("      ", end='')
        elif i >= start and i < end - 1:
            if array[i] == value:
                print("+=====", end='')
            else:
                print("+-----", end='')
        elif i == end - 1:
            if array[i] == value:
                print("+=====+", end='\n')
            else:
                print("+-----+", end='\n')

    for i in range(0, end):
        if i < start:
            print("      ", end='')
        elif i == end-1:
            if array[i] == value:
                print("||" + str(array[i]).zfill(3) + "||", end='\n')
            else:
                print(" " + str(array[i]).zfill(3) + " |", end='\n')
        elif i == start:
            if array[i] == value:
                print("||" + str(array[i]).zfill(3) + "||", end='')
            else:
                print("| " + str(array[i]).zfill(3) + " |", end='')
        elif i > start and i < end-1:
            if array[i] == value:
                print("|" + str(array[i]).zfill(3) + "||", end='')
            else:
                print(" " + str(array[i]).zfill(3) + " |", end='')

    for i in range(0,end):
        if i < start:
            print("      ", end='')
        elif i >= start and i < end - 1:
            if array[i] == value:
                print("+=====", end='')
            else:
                print("+-----", end='')
        elif i == end - 1:
            if array[i] == value:
                print("+=====+", end='\n')
            else:
                print("+-----+", end='\n')

    return

def main():
    arrayNum, searchValue = readInput()
    print("Elemento procurado: " + str(searchValue).zfill(3))
    printArray(arrayNum, 0, len(arrayNum), 1000)
    if IsArrayOrdered(arrayNum) == False:
        print("Vetor nao estah ordenado")
        return
    else:
        binarySearch(arrayNum, searchValue, 0, len(arrayNum))
        return

main()
