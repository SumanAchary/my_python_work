def intersections(arr1, n, arr2, m):
    # Your code goes here
    arr1.sort()
    arr2.sort()
    i = 0
    j = 0
    while i < n and j < m:
        if arr1[i] == arr2[j]:
            print(arr1[i], end=" ")
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
