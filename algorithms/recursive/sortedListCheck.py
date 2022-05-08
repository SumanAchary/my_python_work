def sortedlistCheck(arr, idx):
    length = len(arr)
    if idx == length or idx == length - 1:
        return True
    if arr[idx] > arr[idx + 1]:
        return False
    isSmallerPartSorted = sortedlistCheck(arr, idx + 1)
    return isSmallerPartSorted
