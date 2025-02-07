class Node:
    """A node in the circular linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularQueue:
    """Circular queue implementation using a linked list."""
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, value):
        """Adds an element to the queue."""
        new_node = Node(value)
        if not self.front:
            self.front = self.rear = new_node
            self.rear.next = self.front  # Circular link
        else:
            self.rear.next = new_node
            self.rear = new_node
            self.rear.next = self.front  # Maintain circular connection

    def dequeue(self):
        """Removes and returns the front element from the queue."""
        if not self.front:
            print("Queue is empty!")
            return None
        removed_value = self.front.data
        if self.front == self.rear:  # Single element case
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.rear.next = self.front  # Maintain circular connection
        return removed_value

    def display(self):
        """Displays the elements of the queue."""
        if not self.front:
            print("Queue is empty!")
            return
        temp = self.front
        while True:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.front:
                break
        print()

def demo_circular_queue_linkedlist_based():
    print("==================================")
    print("Demo of linkedlist based circular queue")
    print("==================================")
    # Demo
    queue = CircularQueue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.display()  # Output: 10 20 30
    print("Dequeued:", queue.dequeue())  # Output: 10
    queue.display()  # Output: 20 30
