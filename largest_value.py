
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestValues(self, root: TreeNode):
        if not root:
            return []

        result = []
        queue = [root]  

        while queue:
            level_max = float('-inf')
            next_level = []

            for node in queue:
                level_max = max(level_max, node.val)

                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            result.append(level_max)
            queue = next_level  

        return result
root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(2)
root.left.left = TreeNode(5)
root.left.right = TreeNode(3)
root.right.right = TreeNode(9)
sol = Solution()
output = sol.largestValues(root)
print(output)