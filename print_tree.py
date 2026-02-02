class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]

root = TreeNode(1)
child1=TreeNode(2)
child2=TreeNode(3)
child3=TreeNode(4)

root.childern.append(child1)
root.childern.append(child2)
root.childern.append(child3)

def print_tree(root):
    if (root==None):
        return
    print(root.data)
    for eachchild in root.childern:
        print_tree(eachchild)
print_tree(root)
