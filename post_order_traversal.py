# Post Order Traversal in a tree without recursion

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def post_order_traversal(root):
    if root is None:
        return []

    result = []
    stack = []
    current = root
    visited = set()

    while stack or current:
        if current and current not in visited:
            # Traverse left subtree
            stack.append(current)
            current = current.left
        elif stack:
            # Traverse right subtree
            if stack[-1].right and stack[-1].right not in visited:
                current = stack[-1].right
            else:
                visited.add(stack[-1])
                result.append(stack.pop().value)
        else:
            current = None

    return result

# Example usage:
# Construct a sample binary tree:
#        1
#       / \
#      2   3
#     / \
#    4   5
root = TreeNode(1)
root.left = TreeNode(2) # type: ignore
root.right = TreeNode(3) # type: ignore
root.left.left = TreeNode(4) # type: ignore
root.left.right = TreeNode(5) # type: ignore

result = post_order_traversal(root)
print(result)
