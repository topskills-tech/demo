package data_structures.queue;

import java.util.concurrent.BlockingQueue;
import java.util.concurrent.LinkedBlockingQueue;

/**
 * For thread-safe queues,
 * Java provides BlockingQueue which supports blocking operations
 * (waiting when empty/full).
 * Use Cases:
 *
 * Producer-Consumer Pattern
 * Thread-safe data transfer
 * **/

public class BlockingQueueDemo {
    public static void demo () throws InterruptedException {
        System.out.println("========================");
        System.out.println("BlockingQueue queue demo");
        System.out.println("========================");
        BlockingQueue<Integer> queue = new LinkedBlockingQueue<>(2);

        queue.put(1);
        queue.put(2);
        System.out.println(queue.take()); // Output: 1
    }
}
