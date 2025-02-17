package data_structures.tree;

class RedBlackNode {
    int key;
    RedBlackNode left, right, parent;
    boolean isRed;

    public RedBlackNode(int key) {
        this.key = key;
        this.isRed = true; // New nodes are always red initially
        this.left = this.right = this.parent = null;
    }
}

class RedBlackTree {
    private RedBlackNode root;
    private final RedBlackNode NIL = new RedBlackNode(0);

    public RedBlackTree() {
        root = NIL;
    }

    public void insert(int key) {
        RedBlackNode node = new RedBlackNode(key);
        RedBlackNode parent = null;
        RedBlackNode current = root;

        while (current != NIL) {
            parent = current;
            if (node.key < current.key) {
                current = current.left;
            } else {
                current = current.right;
            }
        }

        node.parent = parent;
        if (parent == null) {
            root = node;
        } else if (node.key < parent.key) {
            parent.left = node;
        } else {
            parent.right = node;
        }

        node.left = NIL;
        node.right = NIL;
        node.isRed = true;

        fixInsert(node);
    }

    private void fixInsert(RedBlackNode node) {
        // Balancing logic after insertion
    }

    public static void demo() {
        RedBlackTree rbt = new RedBlackTree();
        rbt.insert(10);
        rbt.insert(20);
        rbt.insert(15);
    }
}