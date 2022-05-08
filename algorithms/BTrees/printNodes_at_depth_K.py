def printDepthK(root,k):
    if root == None:
        return 0
    if k == 0:
        return root.data 
    printDepthK(root.left,k-1)
    printDepthK(root.right,k-1)