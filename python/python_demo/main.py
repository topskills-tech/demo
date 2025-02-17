# This is a sample Python script.
from data_structures.arrays.array_and_list import demo_array_and_list
from data_structures.hashtables.builtin_hashtables import demo_builtin_hashtables
from data_structures.hashtables.custom_hash_table import demo_custom_hash_table
from data_structures.linked_lists.singly_linked_list import demo_singly_linked_list
from data_structures.queues.array_queue import demo_array_based_queue
from data_structures.queues.built_in_queue import demo_built_in_queues
from data_structures.queues.circular_queue_array_based import demo_circular_queue_array_based
from data_structures.queues.circular_queue_deque import demo_circular_queue_deque
from data_structures.queues.circular_queue_linkedlist_based import demo_circular_queue_linkedlist_based
from data_structures.queues.linkedlist_queue import demo_linked_list_based_queue
from data_structures.stack.array_stack import demo_array_based_stack
from data_structures.stack.builtin_list_based_stack import demo_builtin_list_stack
from data_structures.stack.linkedlist_stack import demo_linkedlist_stack
from data_structures.trees.avl_self_balancing_tree import demo_self_balancing_tree
from data_structures.trees.binary_search_tree import demo_binary_search_tree
from data_structures.trees.binary_tree import demo_binary_tree
from data_structures.trees.red_black_tree import demo_red_black_tree


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def demo():

    #Array
    demo_array_and_list()

    #Linked List
    demo_singly_linked_list()

    #Queue
    demo_array_based_queue()
    demo_linked_list_based_queue()
    demo_built_in_queues()
    demo_circular_queue_array_based()
    demo_circular_queue_deque()
    demo_circular_queue_linkedlist_based()

    #Stack
    demo_array_based_stack()
    demo_linkedlist_stack()
    demo_builtin_list_stack()

    #Hash Table
    demo_builtin_hashtables()
    demo_custom_hash_table()

    #Tree
    demo_binary_tree()
    demo_binary_search_tree()
    demo_self_balancing_tree()
    demo_red_black_tree()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    demo()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
