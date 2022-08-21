
def printNodesWithoutSibling(root) :
    if root == None:
        return
    if root.left is not None and root.right is not None:
        printNodesWithoutSibling(root.left)
        printNodesWithoutSibling(root.right)
    elif root.right is not None:
        print(root.right.data,end = ' ')
        printNodesWithoutSibling(root.right)
    elif root.left is not None:
        print(root.left.data,end = ' ')
        printNodesWithoutSibling(root.left)
