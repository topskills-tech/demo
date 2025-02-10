package stack;

import java.util.Stack;

public class BuiltInStack {

        public static void demo() {
            System.out.println("==============================");
            System.out.println("Demo of Builtin stack");
            System.out.println("==============================");
            Stack<Integer> stack = new Stack<>();

            // Push elements onto the stack
            stack.push(10);
            stack.push(20);
            stack.push(30);

            // Display stack elements
            System.out.println("Stack: " + stack);  // Output: Stack: [10, 20, 30]

            // Peek the top element
            System.out.println("Top element: " + stack.peek());  // Output: 30

            // Pop an element
            System.out.println("Popped: " + stack.pop());  // Output: 30

            // Display stack after popping
            System.out.println("Stack after pop: " + stack);  // Output: [10, 20]
        }
    }
