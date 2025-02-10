package data_structures.hashtables;

import java.util.*;

import java.util.concurrent.ConcurrentHashMap;

public class BuiltInHashTables {
    private HashMap<String, String> hashMapTable;
    private Hashtable<String, String> hashTable;
    private LinkedHashMap<String, String> linkedHashMapTable;
    private ConcurrentHashMap<String, String> concurrentHashTable;

    public BuiltInHashTables() {
        // Initialize different hash table implementations
        hashMapTable = new HashMap<>();
        hashTable = new Hashtable<>();
        linkedHashMapTable = new LinkedHashMap<>();
        concurrentHashTable = new ConcurrentHashMap<>();
    }

    // HashMap methods
    public void hashMapInsert(String key, String value) {
        hashMapTable.put(key, value);
    }

    public String hashMapGet(String key) {
        return hashMapTable.getOrDefault(key, null);
    }

    // Hashtable methods
    public void hashTableInsert(String key, String value) {
        hashTable.put(key, value);
    }

    public String hashTableGet(String key) {
        return hashTable.getOrDefault(key, null);
    }

    // LinkedHashMap methods (maintains insertion order)
    public void linkedHashMapInsert(String key, String value) {
        linkedHashMapTable.put(key, value);
    }

    public String linkedHashMapGet(String key) {
        return linkedHashMapTable.getOrDefault(key, null);
    }

    // ConcurrentHashMap methods (thread-safe)
    public void concurrentHashMapInsert(String key, String value) {
        concurrentHashTable.put(key, value);
    }

    public String concurrentHashMapGet(String key) {
        return concurrentHashTable.getOrDefault(key, null);
    }

    // Display all tables for debugging purposes
    public void displayTables() {
        System.out.println("HashMap Table: " + hashMapTable);
        System.out.println("Hashtable Table: " + hashTable);
        System.out.println("LinkedHashMap Table: " + linkedHashMapTable);
        System.out.println("ConcurrentHashMap Table: " + concurrentHashTable);
    }

    public static void demo() {

        System.out.println("==============================");
        System.out.println("Demo of built in hashtable implementations");
        System.out.println("==============================");
        BuiltInHashTables hashTables = new BuiltInHashTables();

        // Using HashMap
        hashTables.hashMapInsert("name", "Alice");
        System.out.println("HashMap Get: " + hashTables.hashMapGet("name")); // Output: Alice

        // Using Hashtable
        hashTables.hashTableInsert("age", "30");
        System.out.println("Hashtable Get: " + hashTables.hashTableGet("age")); // Output: 30

        // Using LinkedHashMap
        hashTables.linkedHashMapInsert("city", "New York");
        System.out.println("LinkedHashMap Get: " + hashTables.linkedHashMapGet("city")); // Output: New York

        // Using ConcurrentHashMap
        hashTables.concurrentHashMapInsert("country", "USA");
        System.out.println("ConcurrentHashMap Get: " + hashTables.concurrentHashMapGet("country")); // Output: USA

        hashTables.displayTables();
    }
}
