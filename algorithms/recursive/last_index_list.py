def last_index(arr, target):
    l = len(arr)
    if l == 0:
        return -1
    smallerList = arr[1:]
    smallerListOutput = last_index(smallerList, target)
    if smallerListOutput != -1:
        return smallerListOutput + 1
    else:
        if arr[0] == target:
            return 0
        else:
            return -1


print(last_index([3, 2, 5, 8, 1, 2, 332, 2, 4, 3, 3, 1, 1], 8))
