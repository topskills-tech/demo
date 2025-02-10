package stack;

/**
 * Node class representing an element in the linked list-based stack.
 */
class Node {
    int data;
    Node next;

    public Node(int data) {
        this.data = data;
        this.next = null;
    }
}

/**
 * Stack implementation using a linked list.
 */
class LinkedListBasedStack {
    private Node top;  // Pointer to the top element

    /**
     * Pushes an element onto the stack.
     * @param value The value to push onto the stack.
     */
    public void push(int value) {
        Node newNode = new Node(value);
        newNode.next = top;
        top = newNode;
    }

    /**
     * Removes and returns the top element of the stack.
     * @return The popped element, or -1 if the stack is empty.
     */
    public int pop() {
        if (isEmpty()) {
            System.out.println("Stack is empty!");
            return -1;
        }
        int poppedValue = top.data;
        top = top.next;
        return poppedValue;
    }

    /**
     * Returns the top element without removing it.
     * @return The top element, or -1 if the stack is empty.
     */
    public int peek() {
        return isEmpty() ? -1 : top.data;
    }

    /**
     * Checks if the stack is empty.
     * @return True if empty, otherwise false.
     */
    public boolean isEmpty() {
        return top == null;
    }

    /**
     * Displays all elements in the stack.
     */
    public void display() {
        if (isEmpty()) {
            System.out.println("Stack is empty!");
            return;
        }
        Node current = top;
        while (current != null) {
            System.out.print(current.data + " -> ");
            current = current.next;
        }
        System.out.println("None");
    }

    public static void demo() {
        System.out.println("==============================");
        System.out.println("Demo of LinkedList based stack");
        System.out.println("==============================");
        LinkedListBasedStack stack = new LinkedListBasedStack();
        stack.push(10);
        stack.push(20);
        stack.push(30);
        stack.display();  // Output: 30 -> 20 -> 10 -> None
        System.out.println("Top element: " + stack.peek());  // Output: 30
        System.out.println("Popped: " + stack.pop());  // Output: 30
        stack.display();  // Output: 20 -> 10 -> None
    }
}
