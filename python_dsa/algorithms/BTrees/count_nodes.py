class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def numNodes(root):
    if root == None:
        return 0
    leftCount = numNodes(root.left)
    rightCount = numNodes(root.right)
    return 1 + leftCount + rightCount


def printTree(head):
    if head is None:
        return head
    print(head.data, end=":")
    if head.left:
        print("L", head.left.data, end=",")
    if head.right:
        print("R", head.right.data, end="")
    print()
    printTree(head.left)
    printTree(head.right)


one = BinaryTreeNode(1)
two = BinaryTreeNode(2)
three = BinaryTreeNode(3)
four = BinaryTreeNode(4)

one.left = two
one.right = three
one.right.right = four

printTree(one)
