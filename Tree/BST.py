class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
        
def insert(root,key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root 
        elif root.val <key:
            root.right=insert(root.right,key)
        else:
            root.left=insert(root.left,key)
    return root 

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
        
        
        
r=Node(50)
r=insert(r,100)
r=insert(r,70)
r=insert(r,50)
r=insert(r,60)
r=insert(r,9)
r=insert(r,-3)
# r=insert(r,75)
# r=insert(r,78)
inorder(r)