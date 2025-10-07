from collections import deque

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> list[int]:
        if not (y >= x):
            x, y = y, x

        def bfs(start: int) -> list[int]:
            vis = [False] * (n + 1)
            dist = [0] * (n + 1)
            q = deque([start])
            vis[start] = True

            while q:
                curr = q.popleft()
                neighbors = [curr - 1, curr + 1]

                for nbr in neighbors:
                    if 1 <= nbr <= n and not vis[nbr]:
                        vis[nbr] = True
                        dist[nbr] = dist[curr] + 1
                        q.append(nbr)

                if curr == x:
                    if not vis[y]:
                        vis[y] = True
                        dist[y] = dist[curr] + 1
                        q.append(y)
                elif curr == y:
                    if not vis[x]:
                        vis[x] = True
                        dist[x] = dist[curr] + 1
                        q.append(x)

            return dist[1:]

        output = [0] * n

        for i in range(1, n + 1):
            vals = bfs(i)
            for val in vals:
                if val > 0:
                    output[val - 1] += 1

        return output