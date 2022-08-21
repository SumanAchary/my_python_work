# def first_index(arr,targets,si):
#     l = len(arr)
#     if l == 0:
#         return -1
#     if arr[0] == target:
#         return 0
#     if arr[idx] == target:
#         return idx
#     return first_index(arr,target,idx + 1)

# print(first_index([1],0))


def first_index(arr, target, si):
    l = len(arr)
    if l == 0 or l == si:
        return -1
    if arr[si] == target:
        return si

    return first_index(arr, target, si + 1)


print(first_index([3, 2, 5, 2, 1, 2, 332, 2, 4, 3, 3, 1, 1], 8, 0))
