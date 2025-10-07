from collections import deque

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> list[int]:
        result = [0] * n

        def bfs(start: int) -> None:
            visited = [False] * (n + 1)
            distance = [0] * (n + 1)
            queue = deque([start])
            visited[start] = True

            while queue:
                current = queue.popleft()
                for neighbor in [current - 1, current + 1]:
                    if 1 <= neighbor <= n and not visited[neighbor]:
                        visited[neighbor] = True
                        distance[neighbor] = distance[current] + 1
                        queue.append(neighbor)
                if current == x and not visited[y]:
                    visited[y] = True
                    distance[y] = distance[current] + 1
                    queue.append(y)
                if current == y and not visited[x]:
                    visited[x] = True
                    distance[x] = distance[current] + 1
                    queue.append(x)

            for dist in range(1, n + 1):
                if distance[dist] > 0:
                    result[distance[dist] - 1] += 1

        for i in range(1, n + 1):
            bfs(i)

        return result