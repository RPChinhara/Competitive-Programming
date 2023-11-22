# Given an array A of size N which contains elements from 0 to N-1, you need to find all the elements occurring more than once in the given array. Return the answer in ascending order. If no such element is found, return list containing [-1].

def find_duplicate_elements(arr):
    n = len(arr)
    result = []
    
    for i in range(n):
        index = arr[i] % n
        arr[index] += n

    for i in range(n):
        if arr[i] // n > 1:
            result.append(i)

    return result if result else [-1]

# Example usage:
arr = [1, 2, 3, 4, 2, 7, 8, 8, 9, 10]
result = find_duplicate_elements(arr)
print("Duplicate elements:", result)
