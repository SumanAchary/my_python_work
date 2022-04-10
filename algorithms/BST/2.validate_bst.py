# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    return validateBSTHelper(tree, float("-inf"), float("inf"))


def validateBSTHelper(tree, minValue, maxValue):
    if tree is None:
        return True
    if tree.value < minValue or tree.value >= maxValue:
        return False
    left_is_valid = validateBSTHelper(tree.left, minValue, tree.value)
    return left_is_valid and validateBSTHelper(tree.right, tree.value, maxValue)
