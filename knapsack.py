# Knapsack Greedy Problem (maximise profits)

def knapsack_greedy(max_weight, profits, weights):
    n = len(profits)
    if n == 0 or len(weights) != n:
        return 0  # Empty input or unequal lengths of profits and weights.

    items = list(range(n))
    # Sort items by profit in descending order.
    items.sort(key=lambda i: profits[i], reverse=True)

    max_profit = 0
    current_weight = 0

    for item in items:
        if current_weight + weights[item] <= max_weight:
            max_profit += profits[item]
            current_weight += weights[item]

    return max_profit

if __name__=='__main__':
    max_weight = 15
    profits = [10, 5, 15, 7, 6, 18, 3]
    weights = [2, 3, 5, 7, 1, 4, 1]

    result = knapsack_greedy(max_weight, profits, weights)
    print(result)
