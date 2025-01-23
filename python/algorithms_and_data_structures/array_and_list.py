from array import array

# Demonstrating Python arrays
int_array = array('i', [10, 20, 30, 40])  # 'i' means signed integers only
int_array.append(50)  # Add an element
int_array.pop(2)      # Remove the element at index 2
print("Array after operations:", int_array)

# Traversal and searching in an array
for num in int_array:
    print(num, end=" ")
print("\nIndex of 40:", int_array.index(40))

# Demonstrating Python lists
dynamic_list = [1, "hello", 3.14, True]  # Can store mixed types
dynamic_list.append("Python")
dynamic_list.insert(1, "World")  # Insert at index 1
dynamic_list.pop(3)  # Remove the element at index 3
print("\nList after operations:", dynamic_list)

# Traversal and slicing in a list
for item in dynamic_list:
    print(item, end=" ")
print("\nSlice of list (1:3):", dynamic_list[1:3])
