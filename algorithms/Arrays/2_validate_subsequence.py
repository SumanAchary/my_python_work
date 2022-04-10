# given two non-empty arrays of integers, write a function that ditermines whether the second array is a subsequence of the first one.
# array => [5, 1, 22, 25, 6, -1, 8, 10]
# subsequence => [1, 6, -1, 10]


def isValidSubsequence(array, sequence):
    seqIdx = 0
    for val in array:
        if len(sequence) == seqIdx:
            break
        if sequence[seqIdx] == val:
            seqIdx += 1
    return seqIdx == len(sequence)
