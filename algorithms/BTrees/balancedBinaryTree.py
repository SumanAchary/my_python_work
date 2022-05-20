def height(root) :
	#Your code goes here
    if root == None:
        return 0
    left = height(root.left)
    right = height(root.right)
    if left < right:
        h = right + 1
    else:
        h = 1 + left
    return h

def isBalanced(root):
    if root == None:
        return True
    lh = height(root.left)
    rh = height(root.right)
    if lh - rh > 1 or rh - lh > 1:
        return False
    isLeftBalanced = isBalanced(root.left)
    isRightBalanced = isBalanced(root.right)
    if isLeftBalanced and isRightBalanced:
        return True
    else:
        return False