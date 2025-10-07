from collections import deque
from typing import List

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        counts = [0] * n

        def bfs(origin: int) -> None:
            visited = [False] * (n + 1)
            dist = [0] * (n + 1)
            queue = deque([origin])
            visited[origin] = True

            while queue:
                node = queue.popleft()

                neighbors = [node - 1, node + 1]
                for adj in neighbors:
                    if 1 <= adj <= n and not visited[adj]:
                        visited[adj] = True
                        dist[adj] = dist[node] + 1
                        queue.append(adj)

                if node == x and not visited[y]:
                    visited[y] = True
                    dist[y] = dist[node] + 1
                    queue.append(y)

                if node == y and not visited[x]:
                    visited[x] = True
                    dist[x] = dist[node] + 1
                    queue.append(x)

            for idx in range(1, n + 1):
                if dist[idx] > 0:
                    counts[dist[idx] - 1] += 1

        for position in range(1, n + 1):
            bfs(position)

        return counts