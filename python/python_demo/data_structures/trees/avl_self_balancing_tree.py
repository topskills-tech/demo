class AVLNode:
    """A Node in an AVL Tree"""

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    """AVL Tree with self-balancing insert and delete operations"""

    def get_height(self, node):
        """Returns the height of a node"""
        return node.height if node else 0

    def get_balance(self, node):
        """Returns the balance factor of a node"""
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def rotate_right(self, y):
        """Right rotation to balance tree"""
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1

        return x

    def rotate_left(self, x):
        """Left rotation to balance tree"""
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1

        return y

    def insert(self, root, key):
        """Inserts a key while maintaining AVL balance"""
        if not root:
            return AVLNode(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1

        balance = self.get_balance(root)

        # Left Heavy (Right Rotation)
        if balance > 1 and key < root.left.key:
            return self.rotate_right(root)

        # Right Heavy (Left Rotation)
        if balance < -1 and key > root.right.key:
            return self.rotate_left(root)

        # Left-Right Case (Left-Right Rotation)
        if balance > 1 and key > root.left.key:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        # Right-Left Case (Right-Left Rotation)
        if balance < -1 and key < root.right.key:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def inorder_traversal(self, root):
        """Inorder traversal of the AVL tree"""
        if root:
            self.inorder_traversal(root.left)
            print(root.key, end=" ")
            self.inorder_traversal(root.right)

def demo_self_balancing_tree():
    print("==================================")
    print("Demo of an AVL : self balancing tree")
    print("==================================")
    avl_tree = AVLTree()
    root = None

    # Insert elements
    for key in [10, 20, 30, 40, 50, 25]:
        root = avl_tree.insert(root, key)

    print("Inorder traversal of the balanced AVL tree:")
    avl_tree.inorder_traversal(root)  # Output: 10 20 25 30 40 50
