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
        if current.key < key:
            if current.right is None:
                current.size += 1
                current.right = new_node
                new_node.parent = current
                return new_node
            else:
                current.size += 1
                current = current.right
        elif current.key > key:
            if current.left is None:
                current.size += 1
                current.left = new_node
                new_node.parent = current
                return new_node
            else:
                current.size += 1
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

if __name__ == "__main__":
    bst = RankNode()
    for i in range(10):
        insert(bst, i)
    inorder(bst, sizes=True)
            




            
