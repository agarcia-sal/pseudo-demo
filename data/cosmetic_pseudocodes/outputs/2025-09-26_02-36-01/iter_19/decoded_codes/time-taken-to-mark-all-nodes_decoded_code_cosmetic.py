from collections import deque
from typing import List, Dict

class Solution:
    def timeTaken(self, edges: List[List[int]]) -> List[int]:
        count_elements = len(edges) + 1

        # Build adjacency list as a dictionary with default empty lists
        adjacency_map: Dict[int, List[int]] = {i: [] for i in range(count_elements)}
        for u, v in edges:
            adjacency_map[u].append(v)
            adjacency_map[v].append(u)

        def bfs(origin: int) -> int:
            deque_structure = deque()
            deque_structure.append((origin, 0))

            markers = [False] * count_elements
            markers[origin] = True
            peak_time = 0

            while deque_structure:
                position, elapsed = deque_structure.popleft()
                if elapsed > peak_time:
                    peak_time = elapsed

                for adj_node in adjacency_map[position]:
                    if not markers[adj_node]:
                        markers[adj_node] = True
                        val_to_add = 2 if (adj_node % 2 == 0) else 1
                        deque_structure.append((adj_node, elapsed + val_to_add))

            return peak_time

        answers = [0] * count_elements
        for i in range(count_elements):
            answers[i] = bfs(i)

        return answers