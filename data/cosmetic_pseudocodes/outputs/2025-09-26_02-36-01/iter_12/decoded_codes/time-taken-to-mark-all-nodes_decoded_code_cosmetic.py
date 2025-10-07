from collections import deque
from typing import List, Dict

class Solution:
    def timeTaken(self, edges: List[List[int]]) -> List[int]:
        count = len(edges) + 1
        graph: Dict[int, List[int]] = {i: [] for i in range(count)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def bfs(origin: int) -> int:
            dq = deque()
            dq.append((origin, 0))
            visited_flags = [False] * count
            visited_flags[origin] = True
            largest_duration = 0

            while dq:
                current_node, current_time = dq.popleft()
                if largest_duration < current_time:
                    largest_duration = current_time
                for neighbor_node in graph[current_node]:
                    if not visited_flags[neighbor_node]:
                        visited_flags[neighbor_node] = True
                        if neighbor_node % 2 == 0:
                            dq.append((neighbor_node, current_time + 2))
                        else:
                            dq.append((neighbor_node, current_time + 1))
            return largest_duration

        durations = [0] * count
        painter = 0
        while painter <= count - 1:
            durations[painter] = bfs(painter)
            painter += 1

        return durations