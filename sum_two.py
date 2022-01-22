
def two_number_sum(array, target_sum):
    hash_table = {}

    i = 0
    while i < len(array):
        result = target_sum - array[i]
        result_str = str(result)

        if result_str in hash_table:
            return [result, array[i]]
        else:
            current = str(array[i])
            hash_table[current] = i

        i = i + 1

    return []

if __name__ == "__main__":
    print(two_number_sum([3,5,-4,8,11,1,-1,6], 10))