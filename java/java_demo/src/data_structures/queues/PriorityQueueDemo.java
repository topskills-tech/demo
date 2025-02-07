package data_structures.queues;

import java.util.PriorityQueue;

/**
 * Key Characteristics:
 *Unlike normal queues, PriorityQueue orders elements based on priority rather than insertion order.
 * Uses a Min-Heap internally (smallest element at the top).
 * Time complexity: O(log n) for insertion and removal.
 * Can specify a custom comparator for Max-Heap behavior.
 * */
public class PriorityQueueDemo {
    public static void demo() {
        System.out.println("========================");
        System.out.println("PriorityQueue queue demo");
        System.out.println("========================");
        // Min-priority queue
        PriorityQueue<Integer> pq = new PriorityQueue<>();

        // Enqueue elements
        pq.add(3);
        pq.add(1);
        pq.add(2);

        // Dequeue elements
        while (!pq.isEmpty()) {
            System.out.println(pq.poll());  // Output: 1, 2, 3
        }
    }
}