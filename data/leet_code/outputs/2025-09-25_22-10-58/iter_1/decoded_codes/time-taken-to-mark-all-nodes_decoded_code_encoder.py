from collections import deque
from typing import List

class Solution:
    def timeTaken(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1

        # Construct adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def bfs(start: int) -> int:
            queue = deque([(start, 0)])
            visited = [False] * n
            visited[start] = True
            max_time = 0

            while queue:
                current, time = queue.popleft()
                if time > max_time:
                    max_time = time

                for neighbor in adj[current]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        # If neighbor is even, cost is time + 2, else time + 1
                        cost = time + 2 if neighbor % 2 == 0 else time + 1
                        queue.append((neighbor, cost))

            return max_time

        times = [0] * n
        for i in range(n):
            times[i] = bfs(i)

        return times