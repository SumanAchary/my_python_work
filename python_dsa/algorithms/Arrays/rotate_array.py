def rotate(arr, n, d):
    arr[:] = arr[d:n] + arr[0:d]
    return arr
