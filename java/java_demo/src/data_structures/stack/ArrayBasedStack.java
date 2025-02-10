package data_structures.stack;

class ArrayBasedStack {
    private final int[] stack;
    private int top;
    private final int maxSize;

    public ArrayBasedStack(int size) {
        this.maxSize = size;
        this.stack = new int[size];
        this.top = -1;  // Indicates an empty data_structures.stack
    }

    public void push(int data) {
        if (isFull()) {
            throw new RuntimeException("Stack overflow");
        }
        stack[++top] = data;
    }

    public int pop() {
        if (isEmpty()) {
            throw new RuntimeException("Stack is empty");
        }
        return stack[top--];
    }

    public int peek() {
        if (isEmpty()) {
            throw new RuntimeException("Stack is empty");
        }
        return stack[top];
    }

    public boolean isEmpty() {
        return top == -1;
    }

    public boolean isFull() {
        return top == maxSize - 1;
    }

    public int size() {
        return top + 1;
    }

    public static void demo() {
        System.out.println("===============");
        System.out.println("Demo for array based data_structures.stack");
        System.out.println("===============");
        ArrayBasedStack stack = new ArrayBasedStack(5);
        stack.push(10);
        stack.push(20);
        stack.push(30);
        System.out.println("Top element: " + stack.peek());  // Output: 30
        System.out.println("Popped element: " + stack.pop());  // Output: 30
        System.out.println("Stack size: " + stack.size());  // Output: 2
    }
}
