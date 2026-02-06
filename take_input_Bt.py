from collections import deque
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def take_input():
    root = int(input())
    if root == -1:
        return None

    root = Node(root)
    q = deque([root])

    while q:
        curr = q.popleft()

        left = int(input())
        if left != -1:
            curr.left = Node(left)
            q.append(curr.left)

        right = int(input())
        if right != -1:
            curr.right = Node(right)
            q.append(curr.right)

    return root
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)
root = take_input()
inorder(root)
