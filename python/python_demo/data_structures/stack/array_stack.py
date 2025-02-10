class Stack:
    """
    A stack implementation using a Python list (array-based).

    Methods:
        push(data): Adds an element to the top of the stack.
        pop(): Removes and returns the top element.
        peek(): Returns the top element without removing it.
        is_empty(): Checks if the stack is empty.
        size(): Returns the number of elements in the stack.
    """

    def __init__(self):
        self.stack = []

    def push(self, data):
        """Adds an element to the top of the stack."""
        self.stack.append(data)

    def pop(self):
        """
        Removes and returns the top element.

        Raises:
            Exception: If the stack is empty.
        """
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.stack.pop()

    def peek(self):
        """
        Returns the top element without removing it.

        Raises:
            Exception: If the stack is empty.
        """
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.stack[-1]

    def is_empty(self):
        """Checks if the stack is empty."""
        return len(self.stack) == 0

    def size(self):
        """Returns the number of elements in the stack."""
        return len(self.stack)

def demo_array_based_stack():
    # Demo
    print("========================")
    print("Demo of array based stack")
    print("========================")
    # Demo
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    print("Top element:", s.peek())  # Output: 30
    print("Popped element:", s.pop())  # Output: 30
    print("Stack size:", s.size())  # Output: 2
