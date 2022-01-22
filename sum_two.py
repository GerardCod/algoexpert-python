def two_number_sum_pointers(array, target_sum):
    """
        two_number_sum_pointers finds the two numbers whose sum is equals to target_sum
        with the pointers strategy

        array: the collection of numbers that can sum the target number.
        target_num: the target number to find

        returns a list with the two numbers that sums the target number.
        if there are not number that can sum the target, it returns an empty list.

    """
    for i in range(len(array) - 1):
        first_num = array[i]
        
        for j in range(i + 1, len(array)):
            second_num = array[j]
            if first_num + second_num == target_sum:
                return [first_num, second_num]
    return []


def two_number_sum(array, target_sum):
    """
        two_number_sum finds the two numbers whose sum is equals to target_sum

        array: the collection of numbers that can sum the target_sum.
        target_sum: the target number to find

        returns a list with the two numbars that sums the target number.
        if there are not number that can sum the target, it returns an empty list.

    """
    hash_table = {}

    i = 0
    while i < len(array):
        result = target_sum - array[i]

        if result in hash_table:
            return [result, array[i]]
        else:
            current = array[i]
            hash_table[current] = i

        i = i + 1

    return []

if __name__ == "__main__":
    print(two_number_sum([3,5,-4,8,11,1,-1,6], 10))