# Given an array of integers that may contain both positive and negative integers, write a python program to find all pairs whose sum is equal to the desired value.

def find_pairs_with_sum(arr, target_sum):
    pair_set = set()  # A set to store seen numbers

    pairs = []  # List to store pairs that sum to the desired value

    for num in arr:
        # Calculate the complement needed for the current number to reach the target sum
        complement = target_sum - num

        # Check if the complement exists in the dictionary
        if complement in pair_set:
            # If it does, add the pair to the result list
            pairs.append((complement, num))

        # Add the current number to the dictionary with a dummy value
        pair_set.add(num)

    return pairs

arr = [2, 4, 3, 1, 5, 6, -1, 0, 9]
target_sum = 5

result = find_pairs_with_sum(arr, target_sum)
print(result)