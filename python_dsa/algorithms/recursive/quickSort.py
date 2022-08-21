def quickSort(arr, startIdx, endIdx):
    if startIdx >= endIdx:
        return
    pivot_index = partition(arr, startIdx, endIdx)
    quickSort()
    # TODO
