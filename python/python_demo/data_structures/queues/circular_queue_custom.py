class CircularQueue:
    """
    A circular queue implementation using a fixed-size array.

    Attributes:
        size (int): The total capacity of the queue.
        queue (list): The list to hold queue elements.
        front (int): Points to the front element of the queue.
        rear (int): Points to the rear element of the queue.
    """

    def __init__(self, size):
        """
        Initializes the circular queue with the specified size.

        Args:
            size (int): Capacity of the queue.
        """
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1  # Indicating the queue is empty.

    def is_empty(self):
        """Returns True if the queue is empty, else False."""
        return self.front == -1

    def is_full(self):
        """Returns True if the queue is full, else False."""
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, value):
        """
        Enqueue (Insert):

        Adds an element to the rear, ensuring the index wraps around when the end is reached.
        If the queue is full, the element cannot be inserted.

        Args:
            value: The value to add to the queue.

        Raises:
            Exception: If the queue is full.
        """
        if self.is_full():
            raise Exception("Queue is full")

        if self.is_empty():
            self.front = 0  # The queue was empty, so now we have a front.

        self.rear = (self.rear + 1) % self.size  # Move rear in a circular manner.
        self.queue[self.rear] = value

    def dequeue(self):
        """
        Dequeue (Remove):

        Removes an element from the front, with the index wrapping around when it reaches the end.
        If the queue is empty, dequeue cannot be performed.

        Raises:
            Exception: If the queue is empty.
        """
        if self.is_empty():
            raise Exception("Queue is empty")

        value = self.queue[self.front]
        if self.front == self.rear:  # Only one element was in the queue
            self.front = self.rear = -1  # Queue is now empty
        else:
            self.front = (self.front + 1) % self.size  # Move front in a circular manner

        return value

    def peek(self):
        """Returns the front element without removing it."""
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.queue[self.front]

    def display(self):
        """Displays the elements of the queue."""
        if self.is_empty():
            print("Queue is empty.")
        else:
            i = self.front
            while i != self.rear:
                print(self.queue[i], end=" <- ")
                i = (i + 1) % self.size
            print(self.queue[self.rear])


def demo_circular_queue():
    print("========================")
    print("Demo of circular queue")
    print("========================")
    # Demo
    queue = CircularQueue(5)
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.display()  # Output: 10 <- 20 <- 30
    queue.dequeue()
    queue.enqueue(40)
    queue.enqueue(50)
    queue.display()  # Output: 20 <- 30 <- 40 <- 50
    queue.enqueue(60)  # This will wrap around
    queue.display()  # Output: 20 <- 30 <- 40 <- 50 <- 60
