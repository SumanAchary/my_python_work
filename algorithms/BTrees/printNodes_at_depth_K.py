def printDepthK(root,k):
    if root == None:
        return 0
    if k == 0:
        return root.data 
    printDepthK(root.left,k-1)
    printDepthK(root.right,k-1)


def printDepthK_2(root,k,d=0):
    if root == None:
        return 
    if k == d:
        print(root.data)
        return
    printDepthK_2(root.left,k,d+1)
    printDepthK_2(root.right,k,d+1)

