package data_structures.linkedlists;

import java.util.LinkedList;

public class LinkedListDemo {
    public static void demo() {
        demoCustomLinkedList();
        demoJavaLinkedList();
    }

    private static void demoCustomLinkedList() {
        System.out.println("Demo for custom linked list");
        LinkedListCustom ll = new LinkedListCustom();
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

    public static void demoJavaLinkedList(){
        System.out.println("Demo java linked list");
        LinkedList<Integer> list = new LinkedList<>();
        list.add(10);  // Append
        list.add(20);
        list.add(30);
        System.out.println("After appending: " + list);

        list.addFirst(5);  // Prepend
        System.out.println("After prepending: " + list);

        list.remove(Integer.valueOf(20));  // Remove by value
        System.out.println("After deleting 20: " + list);

        System.out.println("First element: " + list.getFirst());
        System.out.println("Last element: " + list.getLast());
    }


}