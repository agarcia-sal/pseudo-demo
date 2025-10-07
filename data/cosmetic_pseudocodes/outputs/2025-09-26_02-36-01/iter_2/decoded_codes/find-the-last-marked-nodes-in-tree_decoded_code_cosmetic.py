from typing import List

class Solution:
    def lastMarkedNodes(self, edges: List[List[int]]) -> List[int]:
        def dfs(current_node: int, parent_node: int, distance_array: List[int]) -> None:
            for neighbor in g[current_node]:
                if neighbor != parent_node:
                    distance_array[neighbor] = distance_array[current_node] + 1
                    dfs(neighbor, current_node, distance_array)

        total_nodes = len(edges) + 1
        g = [[] for _ in range(total_nodes)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        distance_first = [-1] * total_nodes
        distance_first[0] = 0
        dfs(0, -1, distance_first)
        node_a = distance_first.index(max(distance_first))

        distance_second = [-1] * total_nodes
        distance_second[node_a] = 0
        dfs(node_a, -1, distance_second)
        node_b = distance_second.index(max(distance_second))

        distance_third = [-1] * total_nodes
        distance_third[node_b] = 0
        dfs(node_b, -1, distance_third)

        output = []
        for idx in range(total_nodes):
            if distance_second[idx] > distance_third[idx]:
                output.append(node_a)
            else:
                output.append(node_b)

        return output