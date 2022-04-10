# Write a function that takes in non-empty 
# array of the integers that are sorted 
# in ascending order and returns a new 
# arrat of the same length with the 
# squares of the original integers also 
# sorted in ascending order

# "array": [1, 2, 3, 5, 6, 8, 9]
def sortedSquaredArray(array):
    sortedSquares = [0 for _ in array]
	smallerValueIdx = 0
	largerValueIdx = len(array) - 1
	
	for idx in range(len(array)-1,-1,-1):
		smallerValue = array[smallerValueIdx]
		largerValue = array[largerValueIdx]
		
		if abs(smallerValue) > abs(largerValue):
			sortedSquares[idx] = smallerValue ** 2
			smallerValueIdx += 1
		else:
			sortedSquares[idx] = largerValue **2
			largerValueIdx -= 1
	return sortedSquares