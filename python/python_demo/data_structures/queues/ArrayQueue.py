class ArrayQueue:
    """
    A queue implementation using an array (Python list).

    Attributes:
        max_size (int): Maximum size of the queue.
        queue (list): List representing the queue.
        front (int): The index of the front of the queue.
        rear (int): The index of the rear of the queue.
    """

    def __init__(self, max_size):
        """
        Initializes the queue with a fixed size.

        Args:
            max_size (int): Maximum size of the queue.
        """
        self.max_size = max_size
        self.queue = [None] * max_size
        self.front = -1
        self.rear = -1

    def is_empty(self):
        """Checks if the queue is empty."""
        return self.front == -1

    def is_full(self):
        """Checks if the queue is full."""
        return (self.rear + 1) % self.max_size == self.front

    def enqueue(self, value):
        """
        Adds an element to the rear of the queue.

        Args:
            value: The element to add.
        Raises:
            Exception: If the queue is full.
        """
        if self.is_full():
            raise Exception("Queue is full")
        if self.is_empty():
            self.front = 0
        self.rear = (self.rear + 1) % self.max_size
        self.queue[self.rear] = value

    def dequeue(self):
        """
        Removes and returns the front element of the queue.

        Raises:
            Exception: If the queue is empty.
        """
        if self.is_empty():
            raise Exception("Queue is empty")
        value = self.queue[self.front]
        if self.front == self.rear:  # Queue becomes empty
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.max_size
        return value

    def peek(self):
        """Returns the front element without removing it."""
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.queue[self.front]


# Demo
queue = ArrayQueue(5)
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print("Front element:", queue.peek())  # Output: 10
print("Dequeued:", queue.dequeue())  # Output: 10
queue.enqueue(40)
print("Dequeued:", queue.dequeue())  # Output: 20
