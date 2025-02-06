package data_structures.queues;

import java.util.PriorityQueue;

public class PriorityQueueDemo {
    public static void demo() {

        System.out.println("Demo for priority queue");
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