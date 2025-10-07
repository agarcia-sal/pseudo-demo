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
        max_dist = 0

        def dequeue_left(dq: deque) -> Tuple[int, int]:
            return dq.popleft()

        while queue:
            node, dist = dequeue_left(queue)
            if dist > max_dist:
                max_dist = dist
                farthest_node = node

            def mark_and_enqueue(nb: int, cur_dist: int):
                if not visited[nb]:
                    visited[nb] = True
                    queue.append((nb, cur_dist + 1))

            for neighbor in graph[node]:
                mark_and_enqueue(neighbor, dist)

        return farthest_node, max_dist

    def tree_diameter(self, graph: List[List[int]]) -> int:
        start_node = 0
        far_node, _ = self.bfs(graph, start_node)
        _, diameter = self.bfs(graph, far_node)
        return diameter

    def maximum_path_length_from_node(self, graph: List[List[int]], node: int) -> int:
        n = len(graph)
        visited = [False] * n
        queue = deque([(node, 0)])
        visited[node] = True
        max_length = 0

        def remove_left(d: deque) -> Tuple[int, int]:
            return d.popleft()

        while queue:
            current_node, dist = remove_left(queue)
            if dist > max_length:
                max_length = dist

            def add_neighbors(nbr: int, cur_dist: int):
                if not visited[nbr]:
                    visited[nbr] = True
                    queue.append((nbr, cur_dist + 1))

            for neighbor in graph[current_node]:
                add_neighbors(neighbor, dist)

        return max_length

    def minimumDiameterAfterMerge(self, edges1: List[Tuple[int, int]], edges2: List[Tuple[int, int]]) -> int:
        n1 = len(edges1) + 1
        n2 = len(edges2) + 1

        graph1 = [[] for _ in range(n1)]
        graph2 = [[] for _ in range(n2)]

        def append_edge(graph: List[List[int]], u: int, v: int) -> None:
            graph[u].append(v)
            graph[v].append(u)

        for u, v in edges1:
            append_edge(graph1, u, v)
        for u, v in edges2:
            append_edge(graph2, u, v)

        diameter1 = self.tree_diameter(graph1)
        diameter2 = self.tree_diameter(graph2)

        max_paths_graph1 = [self.maximum_path_length_from_node(graph1, i) for i in range(n1)]
        max_paths_graph2 = [self.maximum_path_length_from_node(graph2, j) for j in range(n2)]

        minimum_diameter = inf

        for u in range(n1):
            for v in range(n2):
                candidate = max(diameter1, diameter2, max_paths_graph1[u] + max_paths_graph2[v] + 1)
                if candidate < minimum_diameter:
                    minimum_diameter = candidate

        return minimum_diameter