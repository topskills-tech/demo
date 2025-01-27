package data_structures;

public class LinkedListDemo {
    public static void demo() {
        demoCustomLinkedList();
    }

    private static void demoCustomLinkedList() {
        System.out.println("Demo for custom linked list");
        LinkedList ll = new LinkedList();
        ll.append(10);
        ll.append(20);
        ll.append(30);
        System.out.println("After appending to linked list:");
        ll.display();

        ll.prepend(5);
        System.out.println("After prepending to linked list:");
        ll.display();

        ll.delete(20);
        System.out.println("After deleting 20 from linked list:");
        ll.display();
    }
}