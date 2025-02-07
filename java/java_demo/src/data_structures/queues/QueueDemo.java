package data_structures.queues;

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
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }
    }
}
