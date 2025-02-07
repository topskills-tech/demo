package data_structures.queues;

/**
 * CircularQueue - A fixed-size circular queue implementation using an array.
 * Supports enqueue, dequeue, checking if full/empty, and displaying elements.
 */
public class CircularQueueArrayBased {
    private final int[] queue;  // Array to store queue elements
    private int front;
    private int rear;
    private int size;
    private final int capacity;  // Pointers and size tracker

    /**
     * Constructor to initialize the circular queue.
     * @param capacity Maximum number of elements in the queue.
     */
    public CircularQueueArrayBased(int capacity) {
        this.capacity = capacity;
        queue = new int[capacity];
        front = -1;  // Points to the front element
        rear = -1;   // Points to the last element
        size = 0;    // Number of elements in the queue
    }

    /**
     * Adds an element to the circular queue.
     * @param value The integer value to be inserted.
     */
    public void enqueue(int value) {
        if (isFull()) {
            System.out.println("Queue is full!");
            return;
        }
        if (isEmpty()) {
            front = rear = 0;  // First element case
        } else {
            rear = (rear + 1) % capacity;  // Circular increment
        }
        queue[rear] = value;
        size++;
    }

    /**
     * Removes and returns the front element from the queue.
     * @return The removed element, or -1 if the queue is empty.
     */
    public int dequeue() {
        if (isEmpty()) {
            System.out.println("Queue is empty!");
            return -1;
        }
        int removed = queue[front];
        if (front == rear) { // Only one element left
            front = rear = -1;
        } else {
            front = (front + 1) % capacity;  // Circular increment
        }
        size--;
        return removed;
    }

    /**
     * Checks if the queue is full.
     * @return True if full, otherwise false.
     */
    public boolean isFull() {
        return size == capacity;
    }

    /**
     * Checks if the queue is empty.
     * @return True if empty, otherwise false.
     */
    public boolean isEmpty() {
        return size == 0;
    }

    /**
     * Displays the elements of the queue.
     */
    public void display() {
        if (isEmpty()) {
            System.out.println("Queue is empty!");
            return;
        }
        int index = front;
        while (index != rear) {
            System.out.print(queue[index] + " ");
            index = (index + 1) % capacity;
        }
        System.out.println(queue[index]); // Print last element
    }

    public static void demo() {
        System.out.println("===========================");
        System.out.println("Circular Queue demo based on array");
        System.out.println("===========================");
        CircularQueueArrayBased cq = new CircularQueueArrayBased(5);
        cq.enqueue(10);
        cq.enqueue(20);
        cq.enqueue(30);
        cq.display();  // Output: 10 20 30
        System.out.println("Dequeued: " + cq.dequeue()); // Output: 10
        cq.display();  // Output: 20 30
    }
}
