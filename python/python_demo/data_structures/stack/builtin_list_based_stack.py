class Stack:
    """Stack implementation using Python's built-in list."""
    def __init__(self):
        self.stack = []

    def push(self, value):
        """Pushes an element onto the stack."""
        self.stack.append(value)

    def pop(self):
        """Removes and returns the top element."""
        if self.is_empty():
            print("Stack is empty!")
            return None
        return self.stack.pop()

    def peek(self):
        """Returns the top element without removing it."""
        return None if self.is_empty() else self.stack[-1]

    def is_empty(self):
        """Checks if the stack is empty."""
        return len(self.stack) == 0

    def display(self):
        """Displays all elements in the stack."""
        print("Stack:", self.stack)


def demo_builtin_list_stack():
    print("========================")
    print("Demo of built in list stack ")
    print("========================")
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.display()  # Output: Stack: [10, 20, 30]
    print("Top element:", stack.peek())  # Output: 30
    print("Popped:", stack.pop())  # Output: 30
    stack.display()  # Output: Stack: [10, 20]
