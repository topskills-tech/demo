class Node:

    """
    Represents a single node in a linked list.

    Attributes:
        data: The data stored in the node.
        next: A reference to the next node in the linked list.
    """

    def __init__(self, data):
        self.data = data
        self.next = None  # Points to the next node

class SinglyLinkedList:
    """
    A singly linked list implementation in Python.

    Methods:
        append(data): Adds a node with the specified data at the end of the list.
        prepend(data): Adds a node with the specified data at the beginning of the list.
        delete(data): Deletes the first node containing the specified data.
        display(): Displays the entire linked list as a string representation.
    """
    def __init__(self):
        self.head = None  # The head of the linked list

    def append(self, data):
        """Add a node at the end of the linked list."""
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = new_node
            return
        current = self.head
        while current.next:  # Traverse to the last node
            current = current.next
        current.next = new_node

    def prepend(self, data):
        """Add a node at the beginning of the linked list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        """Delete the first node with the given data."""
        if not self.head:  # If the list is empty
            return
        if self.head.data == data:  # If the head is the node to delete
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        if current.next:  # Node to delete found
            current.next = current.next.next

    def display(self):
        """Print all the nodes in the linked list."""
        nodes = []
        current = self.head
        while current:
            nodes.append(current.data)
            current = current.next
        print(" -> ".join(map(str, nodes)) + " -> NULL")


def demo_singly_linked_list():
    print("==========================")
    print("Demo of Singly linked list")
    print("==========================")
    ll = SinglyLinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    print("After appending:")
    ll.display()
    ll.prepend(5)
    print("After prepending:")
    ll.display()
    ll.delete(20)
    print("After deleting 20:")
    ll.display()

