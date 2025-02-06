package data_structures.queues;

import java.util.ArrayDeque;
import java.util.Queue;

/**
 * Queue Implementation Using ArrayDeque (Recommended Over LinkedList)
 * ArrayDeque is faster than LinkedList because it avoids node-pointer overhead.
 * Why ArrayDeque?
 * Faster than LinkedList for queue operations.
 * Resizable array-backed structure (avoids NullPointerException).
 * */

public class ArrayDequeDemo{
    public static void demo() {
        System.out.println("ArrayDeque queue demo");
        Queue<String> queue = new ArrayDeque<>();

        queue.offer("Alice");
        queue.offer("Bob");
        queue.offer("Charlie");

        System.out.println(queue.poll()); // Output: Alice
        System.out.println(queue.peek()); // Output: Bob
    }
}
