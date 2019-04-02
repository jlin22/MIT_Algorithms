class Node:
    right = None
    left = None
    key = None
    parent = None

def insert(root, key):
    if root.key is None: #empty bst
        root.key = key        
    elif root.key < key:
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

def find(root, key):
    if root is None or root.key == key:
        return root
    elif root.key < key:
        return find(root.right, key)
    elif root.key > key:
        return find(root.left, key)
    
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.key)
    inorder(root.right)

def find_min(root):
    current = root
    while current.left is not None:
        current = current.left
    return current

def next_larger(root):
    if root.right is not None:
        return find_min(root.right)
    else:
        y, x = root.parent, root
        while y is not None and y.right == x:
            x = y
            y = y.parent
        return y

def delete(root):
    if root.right is None or root.left is None:
        if root is root.parent.left:
            root.parent.left = root.right or root.left
            if root.parent.left is not None:
                root.parent.left.parent = root.parent
        else:
            root.parent.right = root.right or root.left
            if root.parent.right is not None:
                root.parent.right.parent = root.parent
        return root
    else:
        s = next_larger(root)
        root.key, s.key = s.key, root.key
        return delete(root)

if __name__ == "__main__":
    bst = Node()
    a = [1, 2, 3, 4, 5]
    for key in a:
        insert(bst, key)
    inorder(bst)
    print('key of find(bst,4):', find(bst, 4).key)
    print('min of bst:',find_min(bst).key)
    print('next larger of find 3:', next_larger(find(bst, 3)).key)
    print('delete 4:', delete(find(bst, 4)))
    print('inorder')
    inorder(bst)
