from predfined_BSTs import create_predefined_bsts_manual
root1, root2, root3 = create_predefined_bsts_manual()
def search_in_BST(root, value):
    if root is None:
        return False
    if root.data == value:
        return True
    if value < root.data:
        return search_in_BST(root.left, value)
    return search_in_BST(root.right, value)
print(search_in_BST(root2, 10))  
print(search_in_BST(root2, 6))   
print(search_in_BST(root2, 99))  
