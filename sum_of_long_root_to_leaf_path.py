# Given a binary tree of size N. Your task is to complete the function sumOfLongRootToLeafPath(), that find the sum of all nodes on the longest path from root to leaf node.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def sum_of_longest_path(root):
    def dfs(node, length, path_sum):
        nonlocal max_length, max_sum

        if not node:
            return

        # Update the current path length and sum
        length += 1
        path_sum += node.data

        # If this is a leaf node and the current path is longer or has a greater sum, update the result
        if not node.left and not node.right:
            if length > max_length or (length == max_length and path_sum > max_sum):
                max_length = length
                max_sum = path_sum

        # Recur for left and right subtrees
        dfs(node.left, length, path_sum)
        dfs(node.right, length, path_sum)

    if not root:
        return 0

    max_length = 0
    max_sum = float('-inf')

    dfs(root, 0, 0)

    return max_sum

# Example Usage:
# Construct a sample binary tree
root = Node(4)
root.left = Node(2) 
root.right = Node(5)
root.left.left = Node(7)
root.left.right = Node(1)
root.right.left = Node(2)
root.right.right = Node(3)
root.left.right.left = Node(6)

result = sum_of_longest_path(root)
print("Sum of nodes on the longest path:", result)
