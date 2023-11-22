# Given an integer K and a queue of integers, we need to reverse the 
# order of the first K elements of the queue, leaving the other elements in the same relative 
# order. 
# Only following standard operations are allowed on queue. 
#      enqueue(x) : Add an item x to rear of queue 
#      dequeue() : Remove an item from front of queue 
#      size() : Returns number of elements in queue. 
#      front() : Finds front item. 
# Note: The above operations represent the general processing’s. In-built functions of 
# the respective languages can be used to solve the problem.

from queue import Queue

def reverse_k_elements(queue, k):
    if k < 0 or k > queue.qsize():
        print("Invalid value of K")
        return

    stack = []

    # Dequeue the first K elements and push them onto the stack
    for _ in range(k):
        stack.append(queue.get())

    # Enqueue the elements from the stack back to the queue
    while stack:
        queue.put(stack.pop())

    # Enqueue the remaining elements (after K) back to the queue
    for _ in range(queue.qsize() - k):
        queue.put(queue.get())

# Example Usage:
k = 3
my_queue = Queue()

# Enqueue elements to the queue
for i in range(1, 6):
    my_queue.put(i)

print("Original Queue:")
while not my_queue.empty():
    print(my_queue.get(), end=" ")

# Reverse the order of the first K elements
reverse_k_elements(my_queue, k)

print("\nQueue after reversing the first", k, "elements:")
while not my_queue.empty():
    print(my_queue.get(), end=" ")
