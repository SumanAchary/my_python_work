def binary_search(array, target, startIdx,endIdx):
    if startIdx > endIdx:
        return -1

    mid = (startIdx + endIdx) // 2

    if array[mid] ==  target:
        return mid
    elif array[mid] > target:
        return binary_search(array,target,startIdx,mid-1)
    else:
        return binary_search(array,target,mid + 1,endIdx)

# [1,2,3,4,5,6,7,8] find => 7
array = [1,2,3,4,5,6,7,8]
print(binary_search(array, 7, 0,len(array)))