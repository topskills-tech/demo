class Node:
    """A Node in a Binary Tree"""
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

class BinaryTree:
    """Basic Binary Tree"""
    def __init__(self, root_key):
        self.root = Node(root_key)

    def inorder_traversal(self, node):
        """Inorder traversal: Left -> Root -> Right"""
        if node:
            self.inorder_traversal(node.left)
            print(node.key, end=" ")
            self.inorder_traversal(node.right)

def demo_binary_tree():
    # Demo
    print("=====================")
    print("Demo of a binary tree")
    print("=====================")
    bt = BinaryTree(10)
    bt.root.left = Node(5)
    bt.root.right = Node(15)
    bt.inorder_traversal(bt.root)  # Output: 5 10 15
    print("\n")