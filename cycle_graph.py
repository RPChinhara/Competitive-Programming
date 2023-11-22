# Given an undirected graph with V vertices and E edges, check whether it contains any cycle or not.

from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def is_cyclic_util(self, v, visited, parent):
        visited[v] = True

        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                if self.is_cyclic_util(neighbor, visited, v):
                    return True
            elif parent != neighbor:
                return True

        return False

    def contains_cycle(self):
        visited = [False] * self.vertices

        for v in range(self.vertices):
            if not visited[v]:
                if self.is_cyclic_util(v, visited, -1):
                    return 1  # The graph contains a cycle

        return 0  # No cycle found

# Example Usage:
# Create a sample graph
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(1, 3)
g.add_edge(3, 4)

result = g.contains_cycle()
print("Does the graph contain a cycle?", result)
