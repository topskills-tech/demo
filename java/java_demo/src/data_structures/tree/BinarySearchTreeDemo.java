package data_structures.tree;



    class BST {
        int key;
        BST left, right;

        public BST(int item) {
            key = item;
            left = right = null;
        }

        void insert(int key) {
            if (key < this.key) {
                if (left == null) left = new BST(key);
                else left.insert(key);
            } else {
                if (right == null) right = new BST(key);
                else right.insert(key);
            }
        }

        boolean search(int key) {
            if (this.key == key) return true;
            else if (key < this.key && left != null) return left.search(key);
            else if (key > this.key && right != null) return right.search(key);
            return false;
        }

        public static void demo() {
            System.out.println("===========================");
            System.out.println("Demo for binary search tree");
            System.out.println("===========================");
            BST bst = new BST(10);
            bst.insert(5);
            bst.insert(15);
            System.out.println(bst.search(5));  // Output: true
            System.out.println(bst.search(20)); // Output: false
            System.out.println("\n");
        }
    }
