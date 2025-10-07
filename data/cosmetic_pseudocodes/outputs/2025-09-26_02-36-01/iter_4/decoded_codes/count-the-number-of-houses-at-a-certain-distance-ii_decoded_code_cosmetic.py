from collections import deque
from typing import List

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        if not (x <= y):
            x, y = y, x

        def bfs(start: int) -> List[int]:
            visited = [False] * (n + 1)
            dist = [0] * (n + 1)
            queue = deque([start])
            visited[start] = True

            while queue:
                curr = queue.popleft()
                adj_nodes = [curr - 1, curr + 1]

                for neighbor in adj_nodes:
                    if 1 <= neighbor <= n and not visited[neighbor]:
                        visited[neighbor] = True
                        dist[neighbor] = dist[curr] + 1
                        queue.append(neighbor)

                if curr == x:
                    if not visited[y]:
                        visited[y] = True
                        dist[y] = dist[curr] + 1
                        queue.append(y)
                elif curr == y:
                    if not visited[x]:
                        visited[x] = True
                        dist[x] = dist[curr] + 1
                        queue.append(x)

            return dist[1:]

        tally = [0] * n
        for i in range(1, n + 1):
            bfs_distances = bfs(i)
            for distance_value in bfs_distances:
                if distance_value > 0:
                    tally[distance_value - 1] += 1

        return tally