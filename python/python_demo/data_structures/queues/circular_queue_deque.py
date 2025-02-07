from collections import deque

class CircularQueue:
    """
    CircularQueue implementation using collections.deque.
    This implementation has a fixed size and supports enqueue and dequeue operations.
    """

    def __init__(self, max_size):
        """
        Initializes a circular queue with a fixed maximum size.
        :param max_size: Maximum number of elements the queue can hold.
        """
        self.queue = deque(maxlen=max_size)

    def enqueue(self, value):
        """
        Adds an element to the circular queue.
        :param value: The value to be added.
        """
        if len(self.queue) == self.queue.maxlen:
            print("Queue is full!")
        else:
            self.queue.append(value)

    def dequeue(self):
        """
        Removes and returns the front element from the queue.
        :return: The removed element or None if the queue is empty.
        """
        if not self.queue:
            print("Queue is empty!")
            return None
        return self.queue.popleft()

    def display(self):
        """
        Displays the current elements in the queue.
        """
        if not self.queue:
            print("Queue is empty!")
        else:
            print("Queue elements:", list(self.queue))



def demo_circular_queue_deque():
    print("========================")
    print("Demo of circular queue with deque from collections ")
    print("========================")
    # Demo
    cq = CircularQueue(3)
    cq.enqueue(10)
    cq.enqueue(20)
    cq.enqueue(30)
    cq.display()  # Output: Queue elements: [10, 20, 30]
    print("Dequeued:", cq.dequeue())  # Output: 10
    cq.display()  # Output: Queue elements: [20, 30]