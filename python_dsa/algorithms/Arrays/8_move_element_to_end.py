# "array": [2, 1, 2, 2, 2, 3, 4, 2],
#   "toMove": 2

def moveElementToEnd(array, toMove):
    idxOne = 0
	idxTwo = len(array) - 1
	
	while( idxOne < idxTwo ):
		while array[idxTwo] == toMove and idxOne < idxTwo :
			idxTwo -= 1
		if array[idxOne] == toMove:
			array[idxOne],array[idxTwo] = array[idxTwo], array[idxOne]
			
		idxOne += 1
		
	return array
		