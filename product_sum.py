def productSum(arr):
    total = 0
    return productSumAux(arr, total)


def productSumAux(arr, total, depth = 1):    
    for element in arr:
        if isList(element):
            total += productSumAux(element, 0, depth + 1)
        else:
            total += element 

    return total * depth


def isList(arr):
    return hasattr(arr, '__len__')


if __name__ == '__main__':
    total = productSum([5, 2, [7, -1], 3, [6, [-13, 8], 4]])
    print(total)