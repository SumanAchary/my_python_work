def findUnique(arr, n):
    dic = {}
    for i in range(n):
        if arr[i] not in dic:
            dic[arr[i]] = 1
        else:
            dic[arr[i]] += 1
    print(dic)
    for j in range(n):
        print("dic[arr[j]]:", dic[arr[j]], "\n")
        if dic[arr[j]] == 1:
            return arr[j]


print(findUnique([1, 2, 2, 3, 3, 1, 6], 7))
