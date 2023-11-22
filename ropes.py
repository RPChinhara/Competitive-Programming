# There are given N ropes of different lengths, we need to connect these ropes into one rope. The cost to connect two ropes is equal to the sum of their lengths. The task is to connect the ropes with minimum cost. Given N size array arr[] contains the lengths of the ropes.

import heapq

def min_cost_to_connect_ropes(arr):
    if len(arr) < 2:
        return 0

    # Convert the input array into a min-heap
    heapq.heapify(arr)

    total_cost = 0

    while len(arr) > 1:
        # Extract the two smallest ropes from the heap
        rope1 = heapq.heappop(arr)
        rope2 = heapq.heappop(arr)

        # Connect the ropes and calculate the cost
        new_rope = rope1 + rope2
        total_cost += new_rope

        # Insert the new rope back into the heap
        heapq.heappush(arr, new_rope)

    return total_cost

# Example Usage:
ropes_lengths = [4, 3, 2, 6]
result = min_cost_to_connect_ropes(ropes_lengths)
print("Minimum cost to connect ropes:", result)
