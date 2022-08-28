def binarySearch(array, target):
    maxPos = len(array) - 1
    minPos = 0
    middlePos = (maxPos + minPos) // 2
    position = -1

    while minPos <= maxPos:
        if array[middlePos] == target:
            position = middlePos
            break
        elif array[middlePos] < target:
            minPos = middlePos + 1
        elif array[middlePos] > target:
            maxPos = middlePos - 1
        
        middlePos = (maxPos + minPos) // 2

    return position


if __name__ == '__main__':
    arr = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
    position = binarySearch(arr, 33)
    print(position)