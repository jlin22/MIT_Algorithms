def height(node):
    if node is None:
        return -1
    else:
        return node.height

def update_height(node):
    node.height = max(height(node.left), height(node.right)) + 1

def rebalance(node):
    while node is not None:
        update_height(node)
        if left_heavy(node):
            if left_heavy(node.left) or balanced(node.left):
                right_rotate(node)
            else:
                left_rotate(node.left)
                right_rotate(node)
        elif right_heavy(node):
            if right_heavy(node.right) or balanced(node.right):
                left_rotate(node)
            else:
                right_rotate(node.right)
                left_rotate(node)
        node = node.parent


