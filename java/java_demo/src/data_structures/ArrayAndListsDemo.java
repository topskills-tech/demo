package data_structures;

import java.util.ArrayList;
import java.util.Arrays;

public  class ArrayAndListsDemo {
    public static void demo() {
        // Arrays
        int[] intArray = {10, 20, 30, 40};  // Fixed size
        System.out.println("Original Array: " + Arrays.toString(intArray));

        // Traversal
        for (int num : intArray) {
            System.out.print(num + " ");
        }

        // Arrays don't support dynamic resizing directly
        int[] resizedArray = Arrays.copyOf(intArray, 5);  // Resize array
        resizedArray[4] = 50;
        System.out.println("\nResized Array: " + Arrays.toString(resizedArray));

        // ArrayList in Java
        ArrayList<String> dynamicList = new ArrayList<>();
        dynamicList.add("Hello");
        dynamicList.add("World");
        dynamicList.add("Java");
        dynamicList.remove(1);  // Remove element at index 1
        dynamicList.add(1, "Programming");  // Insert at index 1
        System.out.println("ArrayList after operations: " + dynamicList);

        // Traversal and search
        for (String str : dynamicList) {
            System.out.print(str + " ");
        }
        System.out.println("\nIndex of 'Java': " + dynamicList.indexOf("Java"));
    }
}
