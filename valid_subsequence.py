def validateSubSequence(array, sequence):
    """
        ### Description
        validateSubSequence -> validates if a sequence of elements is a subsequence of a list.

        ### Parameters
        array: the list where it will validate the subsequence.
        sequence: the potential subsequence of elements

        ### Returns 
        - True when the sequence is a valid subsequence of array.
        - False when the sequence is not a valid subsequence of array.
    """
    arrIdx = 0
    seqIdx = 0

    while arrIdx < len(array) and seqIdx < len(sequence):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        
        arrIdx += 1
    
    return seqIdx == len(sequence)


def validateSubSequenceFor(array, sequence):
    """
        ### Description
        validateSubSequence -> validates if a sequence of elements is a subsequence of a list.

        ### Parameters
        array: the list where it will validate the subsequence.
        sequence: the potential subsequence of elements

        ### Returns 
        - True when the sequence is a valid subsequence of array.
        - False when the sequence is not a valid subsequence of array.
    """
    seqIdx = 0

    for element in array:
        if seqIdx == len(sequence):
            break

        if element == sequence[seqIdx]:
            seqIdx += 1
    
    return seqIdx == len(sequence)


if __name__ == "__main__":
    print(validateSubSequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]))
    print(validateSubSequenceFor([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]))