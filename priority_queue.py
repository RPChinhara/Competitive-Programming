# Implement Priority Queue.

import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []
        heapq.heapify(self.heap)

    def enqueue(self, item, priority):
        heapq.heappush(self.heap, (priority, item))

    def dequeue(self):
        if not self.is_empty():
            return heapq.heappop(self.heap)[1]
        else:
            raise IndexError("Priority queue is empty")

    def is_empty(self):
        return len(self.heap) == 0

# Example Usage:
pq = PriorityQueue()

pq.enqueue("Task 1", 3)
pq.enqueue("Task 2", 1)
pq.enqueue("Task 3", 2)

while not pq.is_empty():
    print("Dequeued:", pq.dequeue())
