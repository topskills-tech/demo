package data_structures.queue;

import java.util.LinkedList;
import java.util.Queue;


/**
 * Key methods
 * add(E e): Adds an element to the queue (throws an exception if full).
 * offer(E e): Adds an element (returns false if full instead of throwing an exception).
 * poll(): Retrieves and removes the front element (returns null if empty).
 * remove(): Similar to poll(), but throws an exception if the queue is empty.
 * peek(): Retrieves the front element without removing it.
 * */

public class LinkedListQueueDemo {
    public static void demo() {
        System.out.println("===========================");
        System.out.println("LinkedList based queue demo");
        System.out.println("===========================");

        Queue<Integer> queue = new LinkedList<>();

        // Enqueue (add elements)
        queue.add(10);
        queue.add(20);
        queue.add(30);

        // Peek (get front element)
        System.out.println("Front: " + queue.peek()); // Output: 10

        // Dequeue (remove elements)
        System.out.println("Removed: " + queue.poll()); // Output: 10
        System.out.println("Front after removal: " + queue.peek()); // Output: 20

        // Check if queue is empty
        System.out.println("Is queue empty? " + queue.isEmpty());
    }
}
