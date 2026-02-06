from collections import deque
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def take_input_levelwise():
    data = int(input())
    if data == -1:
        return None

    root = Node(data)
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
def print_tree(root):
    if root:
        print(root.data, end=" ")
        print_tree(root.left)
        print_tree(root.right)
root = take_input_levelwise()
print_tree(root)
