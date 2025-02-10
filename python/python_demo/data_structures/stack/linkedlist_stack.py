class Node:
    """A node in a linked list-based stack."""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListStack:
    """Stack implementation using a linked list."""
    def __init__(self):
        self.top = None  # Pointer to the top element

    def push(self, value):
        """Pushes an element onto the stack."""
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        """Removes and returns the top element of the stack."""
        if self.is_empty():
            print("Stack is empty!")
            return None
        popped_value = self.top.data
        self.top = self.top.next
        return popped_value

    def peek(self):
        """Returns the top element without removing it."""
        return None if self.is_empty() else self.top.data

    def is_empty(self):
        """Checks if the stack is empty."""
        return self.top is None

    def display(self):
        """Displays all elements in the stack."""
        if self.is_empty():
            print("Stack is empty!")
            return
        current = self.top
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

def demo_linkedlist_stack():
    # Demo
    print("==============================")
    print("Demo of linkedlist based stack")
    print("==============================")
    stack = LinkedListStack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.display()  # Output: 30 -> 20 -> 10 -> None
    print("Top element:", stack.peek())  # Output: 30
    print("Popped:", stack.pop())  # Output: 30
    stack.display()  # Output: 20 -> 10 -> None
