package data_structures.tree;

public class BinarySearchTreeDemo {

    static class Node {
        int key;
        Node left, right;

        public Node(int item) {
            key = item;
            left = right = null;
        }
    }
        Node root;

        public BinarySearchTreeDemo(int key) {
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
            System.out.println("Demo for binary search tree");
            System.out.println("===============");
            BinarySearchTreeDemo bt = new BinarySearchTreeDemo(10);
            bt.root.left = new Node(5);
            bt.root.right = new Node(15);
            bt.inorderTraversal(bt.root); // Output: 5 10 15
        }
    }
