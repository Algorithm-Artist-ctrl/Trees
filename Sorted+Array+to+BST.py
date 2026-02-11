from predfined_BSTs import print_bst

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def print_binary_tree(node):
    if node is None:
        return
    print(f"{node.data}:", end=" ")
    
    if node.left:
        print(f"L->{node.left.data}", end=", ")
    else:
        print("L->None", end=", ")
    
    if node.right:
        print(f"R->{node.right.data}")
    else:
        print("R->None")
    print_binary_tree(node.left)
    print_binary_tree(node.right)

def sortedListToBST(l1):
    if(len(l1)==0):
        return None
    mid = len(l1)//2 
    rootData = l1[mid]
    root = BSTNode(rootData)

    root.left = sortedListToBST(l1[:mid])
    root.right = sortedListToBST(l1[mid+1:])
    return root



root = sortedListToBST([1,2,3,4,5,6,7])
print_binary_tree(root)