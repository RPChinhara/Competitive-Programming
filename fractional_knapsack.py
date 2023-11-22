# Given weights and values of N items, we need to put these items in a knapsack of capacity W to get the maximum total value in the knapsack. 
# Note: Unlike 0/1 knapsack, you are allowed to break the item. 

class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.value_per_weight = value / weight

def fractional_knapsack(items, capacity):
    # Sort items based on value-to-weight ratio in descending order
    items.sort(key=lambda x: x.value_per_weight, reverse=True)

    total_value = 0
    knapsack = [0] * len(items)

    for i in range(len(items)):
        if capacity == 0:
            break

        if items[i].weight <= capacity:
            knapsack[i] = 1  # Take the whole item
            total_value += items[i].value
            capacity -= items[i].weight
        else:
            fraction = capacity / items[i].weight
            knapsack[i] = fraction  # Take a fraction of the item
            total_value += items[i].value * fraction
            capacity = 0

    return knapsack, total_value

# Example Usage:
items = [Item(60, 10), Item(100, 20), Item(120, 30)]
knapsack, max_value = fractional_knapsack(items, 50)

print("Items selected in the knapsack:")
for i in range(len(items)):
    if knapsack[i] > 0:
        print(f"Item {i + 1}: {knapsack[i]:.2f} fraction")

print("Maximum total value in the knapsack:", max_value)
