def merge(a1,a2,a):
    i = 0
    j = 0
    k = 0

    while i < len(a1) and j < len(a2):
        if (a1[i] < a2[j]):
            a[k] = a1[i]
            k += 1
            i += 1
        else:
            a[k] = a2[j]
            k += 1
            j += 1
    while i < len(a1):
        a[k] = a1[i]
        k += 1
        i += 1
    while j < len(a2):
        a[k] = a2[j]
        k += 1
        j += 1

def merge_sort(array):
    if len(array) == 0 or len(array) == 1:
        return
    mid = len(array) // 2
    a1 = array[0:mid]
    a2 = array[mid:]
    merge_sort(a1)
    merge_sort(a2)

    merge(a1,a2,array)

a = [2,4,2,11,6,7,5,4,23423,23,4,2]
merge_sort(a)
print(a)