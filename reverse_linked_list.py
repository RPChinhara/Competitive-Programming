# Write a Program to reverse the Linked List. (Both Iterative and recursive).

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_linked_list_iterative(head):
    prev = None
    current = head

    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev

def reverse_linked_list_recursive(head):
    if head is None or head.next is None:
        return head

    # Recursively reverse the rest of the list
    rest_reversed = reverse_linked_list_recursive(head.next)

    # Change the next of the current node
    head.next.next = head
    head.next = None

    # The new head is the last node of the reversed list
    return rest_reversed


# Example Usage:
# Assume you have a linked list with nodes: 1 -> 2 -> 3 -> 4 -> 5
# Construct the linked list
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

# Reverse the linked list(Iterative)
print("Iterative: ")
new_head = reverse_linked_list_iterative(head)

# Print the reversed linked list
while new_head is not None:
    print(new_head.data, end=" ")
    new_head = new_head.next


# Reverse the linked list(Recursive)
print("Recursive: ")
new_head = reverse_linked_list_recursive(head)

# Print the reversed linked list
while new_head is not None:
    print(new_head.data, end=" ")
    new_head = new_head.next