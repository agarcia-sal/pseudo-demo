from collections import deque

class Solution:
    def countOfPairs(self, n, x, y):
        tally = [0] * n

        def bfs(source):
            seen = [False] * (n + 1)
            dist = [0] * (n + 1)
            q = deque([source])
            seen[source] = True

            while q:
                node = q.popleft()
                for adj in (node - 1, node + 1):
                    if 1 <= adj <= n and not seen[adj]:
                        seen[adj] = True
                        dist[adj] = dist[node] + 1
                        q.append(adj)
                if node == x and not seen[y]:
                    seen[y] = True
                    dist[y] = dist[node] + 1
                    q.append(y)
                if node == y and not seen[x]:
                    seen[x] = True
                    dist[x] = dist[node] + 1
                    q.append(x)

            for d in range(1, n + 1):
                if dist[d] > 0:
                    tally[dist[d] - 1] += 1

        index = 1
        while index <= n:
            bfs(index)
            index += 1

        return tally