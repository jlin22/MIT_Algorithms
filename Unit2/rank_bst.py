class RankNode:
    right = None
    left = None
    parent = None
    size = 1
    key = None

def insert(root, key):
    if root.key is None:
        root.key = key
    new_node = RankNode()
    new_node.key = key
    current = root
    while True:
        current.size += 1
        if current.key < key:
            if current.right is None:
                current.right = new_node
                new_node.parent = current
                return new_node
            else:
                current = current.right
        elif current.key > key:
            if current.left is None:
                current.left = new_node
                new_node.parent = current
                return new_node
            else:
                current = current.left
        else:
            return None

def inorder(root, sizes=False):
    if root is None:
        return
    inorder(root.left, sizes)
    if sizes:
        print(root.key, " size: ", root.size)
    else:
        print(root.key)
    inorder(root.right, sizes)

def delete(root, node):
    if root.left is None or root.right is None:
        if root == root.parent.left:
            root.parent.left = root.left or root.right
            if root.parent.left is not None:
                root.parent.left.parent = root.parent
        else:
            root.parent.right = root.left or root.right
            if root.parent.right is not None:
                root.parent.right = root.parent
        current = root.parent
        while current is not None:
            current.size -= 1
            current = current.parent
    else:
        s = next_larger(root)
        root.key, s.key = s.key, root.key
        return delete(root)

if __name__ == "__main__":
    bst = RankNode()
    for i in range(10):
        insert(bst, i)
    inorder(bst, sizes=True)
            




            
