def isNodePresent(root, x):
    if root == None:
        return
    if root.data == x:
        return True
    res = isNodePresent(root.left, x)
    if res:
        return True
    res2 = isNodePresent(root.right, x)
    return res2
