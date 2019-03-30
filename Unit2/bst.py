class Node:
    right = None
    left = None
    key = None
    parent = None

def insert(root, key):
    if root.key < key:
        if root.right is None:
            root.right = Node()
            root.right.key = key
            root.right.parent = root
            return root.right
        else:
            return insert(root.right, key)
    elif root.key > key:
        if root.left is None:
            root.left = Node()
            root.left.key = key
            root.left.parent = root
            return root.left
        else:
            return insert(root.left, key)
    else:
        return None

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.key)
    inorder(root.right)

if __name__ == "__main__":
    bst = Node()
    a = [1, 2, 3, 4, 5]
    for key in a:
        insert(bst, key)
    inorder(bst)
