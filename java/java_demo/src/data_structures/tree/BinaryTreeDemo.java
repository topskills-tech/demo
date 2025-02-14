package data_structures.tree;

class Node {
    int key;
    Node left, right;

    public Node(int item) {
        key = item;
        left = right = null;
    }
}

public class BinaryTreeDemo {
    Node root;

    public BinaryTreeDemo(int key) {
        root = new Node(key);
    }

    void inorderTraversal(Node node) {
        if (node != null) {
            inorderTraversal(node.left);
            System.out.print(node.key + " ");
            inorderTraversal(node.right);
        }
    }

    public static void demo() {
        System.out.println("===============");
        System.out.println("Demo for binary tree");
        System.out.println("===============");
        BinaryTreeDemo binaryTreeDemo = new BinaryTreeDemo(10);
        binaryTreeDemo.root.left = new Node(5);
        binaryTreeDemo.root.right = new Node(15);
        binaryTreeDemo.inorderTraversal(binaryTreeDemo.root); // Output: 5 10 15
    }
}
