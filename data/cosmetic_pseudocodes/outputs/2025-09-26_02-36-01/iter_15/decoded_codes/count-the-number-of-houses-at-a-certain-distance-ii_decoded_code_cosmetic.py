from collections import deque

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> list[int]:
        if y < x:
            x, y = y, x

        def bfs(start: int) -> list[int]:
            visited = [False] * (n + 1)
            dist = [0] * (n + 1)
            q = deque([start])
            visited[start] = True

            while q:
                curr = q.popleft()
                for nb in (curr - 1, curr + 1):
                    if 1 <= nb <= n and not visited[nb]:
                        visited[nb] = True
                        dist[nb] = dist[curr] + 1
                        q.append(nb)

                if curr == x and not visited[y]:
                    visited[y] = True
                    dist[y] = dist[curr] + 1
                    q.append(y)
                elif curr == y and not visited[x]:
                    visited[x] = True
                    dist[x] = dist[curr] + 1
                    q.append(x)

            return dist[1:]

        ans = [0] * n

        for i in range(1, n + 1):
            vals = bfs(i)
            for v in vals:
                if v > 0:
                    ans[v - 1] += 1

        return ans