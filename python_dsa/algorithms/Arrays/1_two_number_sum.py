# finds the two numbers in array which adds upto targetsum in an optimal way
# "array": [3, 5, -4, 8, 11, 1, -1, 6],
#  "targetSum": 10


def twoNumberSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1

    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum > targetSum:
            right -= 1
        else:
            left += 1
    return []


array = [2, 3, 5, 8, 8, 4, 7, 8, 7, 8, 23, 44]
print(twoNumberSum(array, 2 + 23))
