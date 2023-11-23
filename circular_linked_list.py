# Given head, the head of a singly linked list, find if the linked list is circular or not.

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def is_circular_linked_list(head):
    if not head:
        return True  # An empty linked list is considered circular

    slow_pointer = head
    fast_pointer = head

    while fast_pointer and fast_pointer.next:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next

        if slow_pointer == fast_pointer:
            return True  # There is a cycle in the linked list

    return False  # No cycle found

# Example Usage:
# Assume you have a linked list with nodes: 1 -> 2 -> 3 -> 4 -> 5 -> 2 (making it circular)
# Construct the linked list
head = ListNode(1) # type: ignore
head.next = ListNode(2) # type: ignore
head.next.next = ListNode(3) # type: ignore
head.next.next.next = ListNode(4) # type: ignore
head.next.next.next.next = ListNode(5) # type: ignore
head.next.next.next.next.next = head.next  # Creating a cycle   # type: ignore

# Check if the linked list is circular
result = is_circular_linked_list(head)
if result:
    print("Linked list is circular")
else:
    print("Linked list is not circular")