package data_structures.queue;

public class QueueDemo {

    public static void demo(){
        System.out.println("===============");
        System.out.println("Demo for queues");
        System.out.println("===============");

        try {
            LinkedListQueueDemo.demo();
            ArrayDequeDemo.demo();
            PriorityQueueDemo.demo();
            BlockingQueueDemo.demo();
            CircularQueueArrayBased.demo();
            CircularQueueLinkedListBased.demo();
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }
    }
}
