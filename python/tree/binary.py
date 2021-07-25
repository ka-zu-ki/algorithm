class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    

def insert(node, value):
    if node is None:
        return Node(value)
    
    if value < node.value:
        node.left = insert(node.left, value)
    else:
        node.right = insert(node.right, value)
    return node

def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.value)
        inorder(node.right)

def search(node, value):
    if node is None:
        return False

    if node.value == value:
        return True
    elif node.value > value:
        return search(node.left, value)
    elif node.value < value:
        return search(node.right, value)

def min_value(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def remove(node, value):
    if node is None:
        return node

    if value < node.value:
        node.left = remove(node.left, value)
    elif value > node.value:
        node.right = remove(node.right, value)
    else:
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left

        temp = min_value(node.right)
        node.value = temp.value
        node.right = remove(node.right, temp.value)
    return node


root = None
root = insert(root, 3)
root = insert(root, 6)
root = insert(root, 5)
root = insert(root, 7)
root = insert(root, 1)
print(root.value)
print(root.right.value)
print(root.right.left.value)
print('----------------------')
inorder(root)
print('----------------------')
print(search(root, 7))
print('----------------------')
root = remove(root, 6)
inorder(root)