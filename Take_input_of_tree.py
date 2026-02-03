from print_Tree_detail import TreeNode, print_tree_detail

def take_input():
    data = int(input("Enter data for Node: "))
    node = TreeNode(data)

    num_children = int(input(f"Number of children in {data}: "))

    for _ in range(num_children):
        child = take_input()
        node.children.append(child)   
    return node

root = take_input()
print_tree_detail(root)