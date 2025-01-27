package data_structures;

/**
 * Represents a single node in a linked list.
 *
 * <p>This class contains the data for a node and a reference to the next node.</p>
 */
class Node {
    int data; // The data stored in the node
    Node next; // Reference to the next node

    /**
     * Constructor to create a new node with the specified data.
     *
     * @param data The data to store in the node.
     */
    public Node(int data) {
        this.data = data;
        this.next = null;
    }
}

/**
 * A singly linked list implementation in Java.
 *
 * <p>This class provides methods to manipulate a linked list, including adding,
 * removing, and displaying nodes.</p>
 */
class LinkedListCustom {
    private Node head; // Reference to the first node of the linked list

    /**
     * Appends a new node with the specified data to the end of the linked list.
     *
     * @param data The data for the new node.
     */
    public void append(int data) {
        Node newNode = new Node(data);
        if (head == null) {
            head = newNode;
            return;
        }
        Node current = head;
        while (current.next != null) {
            current = current.next;
        }
        current.next = newNode;
    }

    /**
     * Prepends a new node with the specified data to the beginning of the linked list.
     *
     * @param data The data for the new node.
     */
    public void prepend(int data) {
        Node newNode = new Node(data);
        newNode.next = head;
        head = newNode;
    }

    /**
     * Deletes the first node containing the specified data from the linked list.
     *
     * @param data The data to find and delete in the linked list.
     */
    public void delete(int data) {
        if (head == null) {
            return;
        }
        if (head.data == data) {
            head = head.next;
            return;
        }
        Node current = head;
        while (current.next != null && current.next.data != data) {
            current = current.next;
        }
        if (current.next != null) {
            current.next = current.next.next;
        }
    }

    /**
     * Displays the linked list as a string of nodes.
     */
    public void display() {
        Node current = head;
        while (current != null) {
            System.out.print(current.data + " -> ");
            current = current.next;
        }
        System.out.println("NULL");
    }
}
