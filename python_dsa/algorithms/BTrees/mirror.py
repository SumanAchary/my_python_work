def mirror(root):
    if root == None:
        return None
    mirror(root.left)
    mirror(root.right)
    root.right,root.left = root.left,root.right
    return 



