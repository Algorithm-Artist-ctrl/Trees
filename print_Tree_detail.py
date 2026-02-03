class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

root = TreeNode(1)
child1 = TreeNode(2)
child2 = TreeNode(3)
child3 = TreeNode(4)

root.children.append(child1)
root.children.append(child2)
root.children.append(child3)

def print_tree(root):
    if root is None:
        return
    print(root.data)
    for eachchild in root.children:
        print_tree(eachchild)

def print_tree_detail(root):
    if root is None:
        return

    print(root.data, end=": ")
    for eachchild in root.children:
        print(eachchild.data, end=" ")
    print()

    for eachchild in root.children:
        print_tree_detail(eachchild)
