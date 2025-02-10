package data_structures.hashtables;

class Node {
    String key;
    String value;
    Node next;

    public Node(String key, String value) {
        this.key = key;
        this.value = value;
        this.next = null;
    }
}

public class CustomHashTable {
    private int size;
    private Node[] table;

    public CustomHashTable(int size) {
        this.size = size;
        this.table = new Node[size];
    }

    private int hash(String key) {
        return Math.abs(key.hashCode()) % size;
    }

    public void insert(String key, String value) {
        int index = hash(key);
        if (table[index] == null) {
            table[index] = new Node(key, value);
        } else {
            Node current = table[index];
            while (current != null) {
                if (current.key.equals(key)) {
                    current.value = value; // Update existing key
                    return;
                }
                if (current.next == null) break;
                current = current.next;
            }
            current.next = new Node(key, value);
        }
    }

    public String get(String key) {
        int index = hash(key);
        Node current = table[index];
        while (current != null) {
            if (current.key.equals(key)) {
                return current.value;
            }
            current = current.next;
        }
        return null; // Key not found
    }

    public void delete(String key) {
        int index = hash(key);
        Node current = table[index];
        Node prev = null;

        while (current != null) {
            if (current.key.equals(key)) {
                if (prev != null) {
                    prev.next = current.next;
                } else {
                    table[index] = current.next;
                }
                return;
            }
            prev = current;
            current = current.next;
        }
    }

    public void display() {
        for (int i = 0; i < size; i++) {
            System.out.print("Index " + i + ": ");
            Node current = table[i];
            while (current != null) {
                System.out.print("(" + current.key + ": " + current.value + ") -> ");
                current = current.next;
            }
            System.out.println("None");
        }
    }

    public static void demo() {
        System.out.println("===================");
        System.out.println("Demo for Custom HashTables");
        System.out.println("===================");
        CustomHashTable customTable = new CustomHashTable(10);
        customTable.insert("name", "Alice");
        customTable.insert("age", "30");
        customTable.insert("city", "New York");

        System.out.println("Get name: " + customTable.get("name")); // Output: Alice
        customTable.display();

        customTable.delete("age");
        System.out.println("After deletion:");
        customTable.display();
    }
}

