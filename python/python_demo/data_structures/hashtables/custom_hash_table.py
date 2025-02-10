class Node:
    """Node for linked list used in chaining for collisions."""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None  # Pointer to the next node

class CustomHashTable:
    """Custom hash table implementation using an array of linked lists (chaining for collisions)."""

    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size  # Array to store linked lists

    def _hash(self, key):
        """Generate a hash index for a given key."""
        return hash(key) % self.size

    def insert(self, key, value):
        """Insert a key-value pair into the hash table."""
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = Node(key, value)
        else:
            # Handle collision using chaining
            current = self.table[index]
            while current:
                if current.key == key:
                    current.value = value  # Update existing key
                    return
                if current.next is None:
                    break
                current = current.next
            current.next = Node(key, value)

    def get(self, key):
        """Retrieve a value by key."""
        index = self._hash(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None  # Key not found

    def delete(self, key):
        """Remove a key-value pair from the hash table."""
        index = self._hash(key)
        current = self.table[index]
        prev = None
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next  # Remove head node
                return
            prev, current = current, current.next

    def display(self):
        """Print the current state of the hash table."""
        for i, node in enumerate(self.table):
            if node:
                print(f"Index {i}: ", end="")
                current = node
                while current:
                    print(f"({current.key}: {current.value})", end=" -> ")
                    current = current.next
                print("None")

def demo_custom_hash_table():
    print("=========================")
    print("Demo of custom hash table")
    print("==========================")
    custom_table = CustomHashTable()
    custom_table.insert("name", "Alice")
    custom_table.insert("age", "30")
    custom_table.insert("city", "New York")
    print("Get name:", custom_table.get("name"))  # Output: Alice
    custom_table.display()
    custom_table.delete("age")
    print("After deletion:")
    custom_table.display()
