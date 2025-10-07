from collections import deque

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> list[int]:
        if x > y:
            x, y = y, x

        def bfs(start: int) -> list[int]:
            visited = [False] * (n + 1)
            distance = [0] * (n + 1)
            queue = deque([start])
            visited[start] = True

            while queue:
                current = queue.popleft()
                for neighbor in (current - 1, current + 1):
                    if 1 <= neighbor <= n and not visited[neighbor]:
                        visited[neighbor] = True
                        distance[neighbor] = distance[current] + 1
                        queue.append(neighbor)

                if current == x and not visited[y]:
                    visited[y] = True
                    distance[y] = distance[current] + 1
                    queue.append(y)
                elif current == y and not visited[x]:
                    visited[x] = True
                    distance[x] = distance[current] + 1
                    queue.append(x)

            return distance[1:]

        result = [0] * n
        for i in range(1, n + 1):
            distances = bfs(i)
            for d in distances:
                if d > 0:
                    result[d - 1] += 1

        return result