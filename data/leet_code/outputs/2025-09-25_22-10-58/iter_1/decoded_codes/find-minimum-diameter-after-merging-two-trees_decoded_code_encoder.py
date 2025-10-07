from collections import deque
from math import inf
from typing import List, Tuple

class Solution:
    def bfs(self, graph: List[List[int]], start: int) -> Tuple[int, int]:
        n = len(graph)
        visited = [False] * n
        queue = deque([(start, 0)])
        visited[start] = True
        farthest_node = start
        max_distance = 0

        while queue:
            node, distance = queue.popleft()
            if distance > max_distance:
                max_distance = distance
                farthest_node = node

            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor, distance + 1))

        return farthest_node, max_distance

    def tree_diameter(self, graph: List[List[int]]) -> int:
        start_node = 0
        farthest_node, _ = self.bfs(graph, start_node)
        _, diameter = self.bfs(graph, farthest_node)
        return diameter

    def maximum_path_length_from_node(self, graph: List[List[int]], node: int) -> int:
        n = len(graph)
        visited = [False] * n
        queue = deque([(node, 0)])
        visited[node] = True
        max_distance = 0

        while queue:
            curr_node, distance = queue.popleft()
            if distance > max_distance:
                max_distance = distance

            for neighbor in graph[curr_node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor, distance + 1))

        return max_distance

    def minimumDiameterAfterMerge(
        self,
        edges1: List[Tuple[int, int]],
        edges2: List[Tuple[int, int]],
    ) -> int:
        n = len(edges1) + 1
        m = len(edges2) + 1

        graph1 = [[] for _ in range(n)]
        graph2 = [[] for _ in range(m)]

        for u, v in edges1:
            graph1[u].append(v)
            graph1[v].append(u)

        for u, v in edges2:
            graph2[u].append(v)
            graph2[v].append(u)

        diameter1 = self.tree_diameter(graph1)
        diameter2 = self.tree_diameter(graph2)

        longest_path_from_each_node1 = [
            self.maximum_path_length_from_node(graph1, i) for i in range(n)
        ]
        longest_path_from_each_node2 = [
            self.maximum_path_length_from_node(graph2, i) for i in range(m)
        ]

        min_diameter = inf
        for u in range(n):
            for v in range(m):
                new_diameter = max(
                    diameter1,
                    diameter2,
                    longest_path_from_each_node1[u] + longest_path_from_each_node2[v] + 1,
                )
                if new_diameter < min_diameter:
                    min_diameter = new_diameter

        return min_diameter