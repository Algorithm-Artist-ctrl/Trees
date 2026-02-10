class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def print_bst(root):
    """In-order traversal"""
    if root is None:
        return
    print_bst(root.left)
    print(root.data, end=" ")
    print_bst(root.right)


def create_predefined_bsts_manual():
    # BST 1
    root1 = BSTNode(10)
    root1.left = BSTNode(5)
    root1.right = BSTNode(15)
    root1.left.left = BSTNode(2)
    root1.left.right = BSTNode(7)
    root1.right.right = BSTNode(20)

    # BST 2
    root2 = BSTNode(8)
    root2.left = BSTNode(3)
    root2.right = BSTNode(12)
    root2.left.left = BSTNode(1)
    root2.left.right = BSTNode(6)
    root2.right.left = BSTNode(10)
    root2.right.right = BSTNode(14)

    # BST 3
    root3 = BSTNode(50)
    root3.left = BSTNode(30)
    root3.right = BSTNode(70)
    root3.left.left = BSTNode(20)
    root3.left.right = BSTNode(40)
    root3.right.left = BSTNode(60)
    root3.right.right = BSTNode(80)

    return root1, root2, root3
