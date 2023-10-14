# Given an array of n integers where each element represents the maximum length of the jump that can be made forward from that element. 
# This means if array[i] is equal to x, then we can jump any distance y, such that y less than or equal to x. 
# Find the minimum no. of jumps to reach the end of the array starting from the first element. 
# If an element is zero, then you can't move to the next element

def min_jumps_to_end(arr):
    n = len(arr)
    if n <= 1:
        return 0  # If the array has 0 or 1 elements, no jumps are needed.

    jumps = [0] * n  # Initialize an array to store the minimum jumps for each position.
    
    for i in range(1, n):
        # Initialize to positive infinity initially.
        jumps[i] = float('inf')  # type: ignore 

        for j in range(i):
            if i <= j + arr[j] and jumps[j] != float('inf'):
                # If we can jump from position j to i and it's not an unreachable position:
                jumps[i] = min(jumps[i], jumps[j] + 1)
    
    if jumps[n - 1] == float('inf'):
        return -1  # If the last position is unreachable, return -1.

    return jumps[n - 1]


arr = [2, 3, 1, 1, 4]
result = min_jumps_to_end(arr)

if result == -1:
    print('End of Array is unreachable')
else:
    print(result)  # Output: 2 (Jump from index 0 to index 1, and then from index 1 to the end)