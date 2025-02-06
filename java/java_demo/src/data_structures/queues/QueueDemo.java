package data_structures.queues;

public class QueueDemo {

    public static void demo(){
        System.out.println("Demo for queues");

        try {
            LinkedListQueueDemo.demo();
            ArrayDequeDemo.demo();
            PriorityQueueDemo.demo();
            BlockingQueueDemo.demo();
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }
    }
}
