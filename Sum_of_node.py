class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def sum_of_nodes(root):
    if root is None:
        return 0
    return root.value + sum_of_nodes(root.left) + sum_of_nodes(root.right)
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

print(sum_of_nodes(root)) 
