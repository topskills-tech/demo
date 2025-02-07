package data_structures.queues;

public class CircularQueueLinkedListBased {
    private static class Node {
        int data;
        Node next;
        public Node(int data) { this.data = data; }
    }

    private Node front, rear;

    /**
     * Inserts an element into the circular queue.
     * @param value Value to be added.
     */
    public void enqueue(int value) {
        Node newNode = new Node(value);
        if (front == null) {
            front = rear = newNode;
            rear.next = front;  // Circular link
        } else {
            rear.next = newNode;
            rear = newNode;
            rear.next = front;  // Maintain circular connection
        }
    }

    /**
     * Removes and returns the front element from the queue.
     * @return The removed element, or -1 if the queue is empty.
     */
    public int dequeue() {
        if (front == null) {
            System.out.println("Queue is empty!");
            return -1;
        }
        int removedValue = front.data;
        if (front == rear) { // Single element case
            front = rear = null;
        } else {
            front = front.next;
            rear.next = front;  // Maintain circular connection
        }
        return removedValue;
    }

    /**
     * Displays the elements of the queue.
     */
    public void display() {
        if (front == null) {
            System.out.println("Queue is empty!");
            return;
        }
        Node temp = front;
        do {
            System.out.print(temp.data + " ");
            temp = temp.next;
        } while (temp != front);
        System.out.println();
    }

    public static void demo() {
        System.out.println("===========================");
        System.out.println("Circular Queue demo based on LinkedList");
        System.out.println("===========================");
        CircularQueueLinkedListBased queue = new CircularQueueLinkedListBased();
        queue.enqueue(10);
        queue.enqueue(20);
        queue.enqueue(30);
        queue.display();  // Output: 10 20 30
        System.out.println("Dequeued: " + queue.dequeue());  // Output: 10
        queue.display();  // Output: 20 30
    }
}
