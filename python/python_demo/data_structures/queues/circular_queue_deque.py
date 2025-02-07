from collections import deque

def demo_circular_queue_deque():
    print("========================")
    print("Demo of circular queue with deque from collections ")
    print("========================")
    # Demo
    cq = deque(maxlen=5)
    cq.append(10)
    cq.append(20)
    cq.append(30)
    print(list(cq))  # Output: [10, 20, 30]
    cq.popleft()     # Removes first element (FIFO)
    print(list(cq))  # Output: [20, 30]
