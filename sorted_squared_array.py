def sortedSquaredArray(array):
    """
        ### Description
        sortedSquaredArray takes an array and squares every number in and returns a 
        new list sorted in ascending order.

        ### Parameters
        - array: The collection of numbers.

        ### Returns
        A new sorted list in an ascending way containing the squares of every number of the array param. 
    """
    squared = []
    for number in array:
        squared.append(number ** 2)
    
    squared.sort()
    return squared


def sortedSquaredArrayPointers(array):
    """
        ### Description
        sortedSquaredArray takes an array and squares every number in and returns a 
        new list sorted in ascending order.

        ### Parameters
        - array: The collection of numbers.

        ### Returns
        A new sorted list in an ascending way containing the squares of every number of the array param. 
    """
    squared = [0 for _ in array]

    start = 0
    end = len(array) - 1
    idx = len(array) - 1

    while start <= end:
        if abs(array[start]) < abs(array[end]):
            squared[idx] = array[end] ** 2
            end -= 1
        else:
            squared[idx] = array[start] ** 2
            start += 1
        idx -= 0

    return squared


if __name__ == "__main__":
    print(sortedSquaredArray([-5, -4, -3, -2, -1]))