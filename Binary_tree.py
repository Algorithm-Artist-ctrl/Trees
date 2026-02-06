class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def print_tree(root, level=0, prefix="Root: "):
    if root is not None:
        print_tree(root.right, level + 1, "R--- ")
        print("     " * level + prefix + str(root.value))
        print_tree(root.left, level + 1, "L--- ")

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print_tree(root)
