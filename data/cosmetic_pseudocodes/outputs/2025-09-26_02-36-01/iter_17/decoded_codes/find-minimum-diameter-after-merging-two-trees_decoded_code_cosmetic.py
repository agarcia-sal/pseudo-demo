from collections import deque
from math import inf
from typing import List, Tuple

class Solution:
    def bfs(self, graph: List[List[int]], start: int) -> Tuple[int, int]:
        n = len(graph)
        visited = [False] * n
        queue = deque()
        queue.append((start, 0))
        visited[start] = True
        farthest_node = start
        max_distance = 0

        while queue:
            node, dist = queue.popleft()
            if dist > max_distance:
                max_distance = dist
                farthest_node = node
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor, dist + 1))
        return farthest_node, max_distance

    def tree_diameter(self, graph: List[List[int]]) -> int:
        start = 0
        far_node, _ = self.bfs(graph, start)
        _, diameter = self.bfs(graph, far_node)
        return diameter

    def maximum_path_length_from_node(self, graph: List[List[int]], node: int) -> int:
        n = len(graph)
        visited = [False] * n
        queue = deque()
        queue.append((node, 0))
        visited[node] = True
        max_length = 0

        while queue:
            curr, dist = queue.popleft()
            if dist > max_length:
                max_length = dist
            for neighbor in graph[curr]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor, dist + 1))
        return max_length

    def minimumDiameterAfterMerge(self, edges1: List[Tuple[int, int]], edges2: List[Tuple[int, int]]) -> int:
        n1 = len(edges1) + 1
        n2 = len(edges2) + 1

        graph1 = [[] for _ in range(n1)]
        graph2 = [[] for _ in range(n2)]

        for u, v in edges1:
            graph1[u].append(v)
            graph1[v].append(u)

        for u, v in edges2:
            graph2[u].append(v)
            graph2[v].append(u)

        diameter1 = self.tree_diameter(graph1)
        diameter2 = self.tree_diameter(graph2)

        max_path_1 = [self.maximum_path_length_from_node(graph1, i) for i in range(n1)]
        max_path_2 = [self.maximum_path_length_from_node(graph2, i) for i in range(n2)]

        min_diameter = inf
        for i in range(n1):
            for j in range(n2):
                merged_path_len = max_path_1[i] + max_path_2[j] + 1
                candidate = max(diameter1, diameter2, merged_path_len)
                if candidate < min_diameter:
                    min_diameter = candidate

        return min_diameter