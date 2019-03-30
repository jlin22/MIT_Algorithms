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

def left_heavy(node):
    return height(node.left) > height(node.right) + 1

def right_heavy(node):
    return height(node.right) > height(node.left) + 1

def balanced(node):
    return height(node.right) == height(node.left)

def left_rotate(node):
    prev_key = node.key
    node.key = node.right.key
    prev_right_left = node.right.left
    node.right = node.right.right
    node.left.parent = Node()
    node.left = node.left.parent
    node.left.key = prev_key
    node.left.right = prev_right_left

def left_rotate_better(node):
    prev_right_left = node.right.left
    node.right.parent = node.parent
    node.parent = node.right
    node.right.left = node
    node.right = prev_right_left

def right_rotate(node):
    prev_left_right = node.left.right
    node.left.parent = node.parent
    node.parent = node.left
    node.left.right = node
    node.left = prev_left_right

