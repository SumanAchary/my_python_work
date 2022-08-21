def numLeafNodes(root):
    if root == None:
        return 0
    if root.left == None and root.right == None:
        return 1
    numLeafLeft = numLeafNodes(root.left)
    numLeafRight = numLeafNodes(root.right)
    return numLeafLeft + numLeafRight
