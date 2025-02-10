class Node:
    """
    Represents a node in the linked list.

    Attributes:
        data: The value stored in the node.
        next: A reference to the next node.
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListQueue:
    """
    A queue implementation using a linked list.

    Attributes:
        front (Node): The front node of the queue.
        rear (Node): The rear node of the queue.
    """

    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        """Checks if the queue is empty."""
        return self.front is None

    def enqueue(self, value):
        """
        Adds an element to the rear of the queue.

        Args:
            value: The element to add.
        """
        new_node = Node(value)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        """
        Removes and returns the front element of the queue.

        Raises:
            Exception: If the queue is empty.
        """
        if self.is_empty():
            raise Exception("Queue is empty")
        value = self.front.data
        self.front = self.front.next
        if self.front is None:  # If the queue becomes empty
            self.rear = None
        return value

    def peek(self):
        """Returns the front element without removing it."""
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.front.data


def demo_linked_list_based_queue():
    print("========================")
    print("Demo of linkedlist based queue")
    print("========================")
    # Demo
    queue = LinkedListQueue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print("Front element:", queue.peek())  # Output: 10
    print("Dequeued:", queue.dequeue())  # Output: 10
    queue.enqueue(40)
    print("Dequeued:", queue.dequeue())  # Output: 20
