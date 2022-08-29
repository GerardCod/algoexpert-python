def bubbleSort(array):
    sortedList = [num for num in array]

    i = 0
    length = len(sortedList)

    while i < length - 1:
      j = 0
      while j < length - 1:
        if sortedList[j] > sortedList[j + 1]:
            sortedList[j], sortedList[j + 1] = sortedList[j + 1], sortedList[j]
        j += 1
      i += 1
    
    return sortedList


if __name__ == '__main__':
    sortedList = bubbleSort([8, 5, 2, 9, 5, 6, 3])
    print(sortedList)