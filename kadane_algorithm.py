# Write a program explaining Kadane’s Algorithm in simpler terms.

def kadanes_algorithm(arr):
    if not arr:
        return 0
    
    max_sum = arr[0]
    current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = kadanes_algorithm(arr)
print("Maximum sum of contiguous subarray:", result)
