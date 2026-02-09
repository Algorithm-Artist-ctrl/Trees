class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def sum_of_left_leaves(root):
    if root is None:
        return 0
    total = 0
    if root.left and not root.left.left and not root.left.right:
        total += root.left.val
    total += sum_of_left_leaves(root.left)
    total += sum_of_left_leaves(root.right)
    return total
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20, TreeNode(15), TreeNode(7))
print(sum_of_left_leaves(root))  
