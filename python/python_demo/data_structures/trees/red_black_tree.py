class Node:
    """A Node in a Red-Black Tree"""
    def __init__(self, key, color="RED"):
        self.key = key
        self.color = color  # "RED" or "BLACK"
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    """Red-Black Tree Implementation"""
    def __init__(self):
        self.NIL = Node(0, "BLACK")
        self.root = self.NIL

    def insert(self, key):
        """Insert a node into the Red-Black Tree"""
        node = Node(key)
        node.left = self.NIL
        node.right = self.NIL
        parent = None
        current = self.root

        while current != self.NIL:
            parent = current
            if node.key < current.key:
                current = current.left
            else:
                current = current.right

        node.parent = parent
        if not parent:
            self.root = node
        elif node.key < parent.key:
            parent.left = node
        else:
            parent.right = node

        node.color = "RED"
        self.fix_insert(node)

    def fix_insert(self, node):
        """Balance the tree after insertion"""
        pass  # Implementation of balancing logic here

    def inorder_traversal(self, node):
        if node != self.NIL:
            self.inorder_traversal(node.left)
            print(node.key, "(", node.color, ")", end=" ")
            self.inorder_traversal(node.right)

def demo_red_black_tree():
    print("=========================")
    print("Demo of an red black tree")
    print("=========================")
    rbt = RedBlackTree()
    rbt.insert(10)
    rbt.insert(20)
    rbt.insert(15)
    rbt.inorder_traversal(rbt.root)