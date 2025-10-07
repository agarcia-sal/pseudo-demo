from collections import deque

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> list[int]:
        if not (x <= y):
            x, y = y, x

        def bfs(start: int) -> list[int]:
            visited = [False] * (n + 1)
            dist = [0] * (n + 1)
            queue = deque([start])
            visited[start] = True

            while True:
                if not queue:
                    break
                curr = queue.popleft()

                for neighbor in (curr - 1, curr + 1):
                    if 1 <= neighbor <= n and not visited[neighbor]:
                        visited[neighbor] = True
                        dist[neighbor] = dist[curr] + 1
                        queue.append(neighbor)

                if curr == x:
                    if not visited[y]:
                        visited[y] = True
                        dist[y] = dist[curr] + 1
                        queue.append(y)
                else:
                    if curr == y and not visited[x]:
                        visited[x] = True
                        dist[x] = dist[curr] + 1
                        queue.append(x)

            return dist[1:]

        output = [0] * n

        def processDistances(arr: list[int]) -> None:
            for d in arr:
                if d > 0:
                    output[d - 1] += 1

        for i in range(1, n + 1):
            valList = bfs(i)
            processDistances(valList)

        return output