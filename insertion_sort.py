def insertionSort(array):
    sortedList = [num for num in array]
    i = 0
    length = len(array)

    while i < length - 1:
        j = i
        while j < length - 1:
            if sortedList[i] > sortedList[j + 1]:
                sortedList[i], sortedList[j + 1] = sortedList[j + 1], sortedList[i]
            j += 1
        i += 1

    return sortedList


if __name__ == '__main__':
    sortedList = insertionSort([8, 5, 2, 9, 5, 6, 3])
    print(sortedList)

    