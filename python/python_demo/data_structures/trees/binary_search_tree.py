class BST:
    """Binary Search Tree Implementation"""
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, key):
        if key < self.key:
            if self.left:
                self.left.insert(key)
            else:
                self.left = BST(key)
        else:
            if self.right:
                self.right.insert(key)
            else:
                self.right = BST(key)

    def search(self, key):
        if self.key == key:
            return True
        elif key < self.key and self.left:
            return self.left.search(key)
        elif key > self.key and self.right:
            return self.right.search(key)
        return False

def demo_binary_search_tree():
    # Demo
    print("============================")
    print("Demo of a binary search tree")
    print("============================")
    bst = BST(10)
    bst.insert(5)
    bst.insert(15)
    print(bst.search(5))  # Output: True
    print(bst.search(20)) # Output: False