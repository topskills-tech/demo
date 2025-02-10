from collections import OrderedDict, defaultdict

class BuiltInHashTables:
    """A class demonstrating different built-in hash table implementations in Python."""

    def __init__(self):
        # Initialize different types of hash tables
        self.dict_table = {}
        self.ordered_dict_table = OrderedDict()
        self.default_dict_table = defaultdict(lambda: "Default Value")

    def dict_insert(self, key, value):
        """Insert a key-value pair into a Python dictionary."""
        self.dict_table[key] = value

    def dict_get(self, key):
        """Retrieve a value from a Python dictionary."""
        return self.dict_table.get(key, None)

    def ordered_dict_insert(self, key, value):
        """Insert a key-value pair into an OrderedDict (maintains insertion order)."""
        self.ordered_dict_table[key] = value

    def ordered_dict_get(self, key):
        """Retrieve a value from an OrderedDict."""
        return self.ordered_dict_table.get(key, None)

    def default_dict_insert(self, key, value):
        """Insert a key-value pair into a defaultdict."""
        self.default_dict_table[key] = value

    def default_dict_get(self, key):
        """Retrieve a value from a defaultdict (returns default value if key is missing)."""
        return self.default_dict_table[key]  # Will return default if key doesn't exist

    def display_tables(self):
        """Print all tables for debugging purposes."""
        print("Dict Table:", self.dict_table)
        print("OrderedDict Table:", self.ordered_dict_table)
        print("DefaultDict Table:", self.default_dict_table)


# Example Usage
def demo_builtin_hashtables():
    print("============================")
    print("Demo of built in hash tables")
    print("============================")
    hash_tables = BuiltInHashTables()

    # Using dict
    hash_tables.dict_insert("name", "Alice")
    print("Dict Get:", hash_tables.dict_get("name"))  # Output: Alice

    # Using OrderedDict
    hash_tables.ordered_dict_insert("age", 30)
    print("OrderedDict Get:", hash_tables.ordered_dict_get("age"))  # Output: 30

    # Using defaultdict
    hash_tables.default_dict_insert("city", "New York")
    print("DefaultDict Get (existing key):", hash_tables.default_dict_get("city"))  # Output: New York
    print("DefaultDict Get (missing key):", hash_tables.default_dict_get("country"))  # Output: Default Value

    hash_tables.display_tables()
