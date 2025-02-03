
from collections import deque
from queue import Queue


def demo_deque_queue():
    global queue
    print("deque implementation of a queue")
    # Initialize a deque as a queue
    queue = deque()
    # Enqueue elements
    queue.append(10)
    queue.append(20)
    queue.append(30)
    # Peek the front element
    print("Front element:", queue[0])  # Output: 10
    # Dequeue elements
    print("Dequeued:", queue.popleft())  # Output: 10
    queue.append(40)
    print("Dequeued:", queue.popleft())  # Output: 20





def demo_queue_queue():
    global queue
    print("Queue implementation of a queue")
    # Initialize a thread-safe queue
    queue = Queue()
    # Enqueue elements
    queue.put(10)
    queue.put(20)
    queue.put(30)
    # Peek the front element (no direct method, but you can dequeue and check)
    print("Front element:", queue.queue[0])  # Output: 10
    # Dequeue elements
    print("Dequeued:", queue.get())  # Output: 10
    queue.put(40)
    print("Dequeued:", queue.get())  # Output: 20


def demo_built_in_queues():
    print("========================")
    print("Demo of built in queues")
    print("========================")
    demo_queue_queue()
    demo_deque_queue()


