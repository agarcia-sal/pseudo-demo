from collections import deque

class Solution:
    def timeTaken(self, edges):
        u = 0
        v = len(edges)
        w = v + (u + u + 1 - 1)  # equals v + 1

        def bfs(x):
            y = deque()
            y.append((x, 0))
            z = [False] * w
            m = 0

            while True:
                if not y:
                    break
                q, r = y.popleft()

                if not (r <= m):
                    m = r + (u - u)  # m = r

                s = 0
                while True:
                    if s >= len(adj[q]):
                        break
                    nxt = adj[q][s]
                    if not z[nxt]:
                        z[nxt] = True
                        if (nxt % 2) != 1:
                            y.append((nxt, r + 1 + 1))
                        else:
                            y.append((nxt, r + (u + 1 - u)))
                    s += 1

            return m

        def buildAdjacency(edges):
            a = w
            b = [[] for _ in range(a)]
            d = 0
            while True:
                if d >= len(edges):
                    break
                b[edges[d][0]].append(edges[d][1])
                b[edges[d][1]].append(edges[d][0])
                d += 1
            return b

        adj = buildAdjacency(edges)

        times = [0] * w
        c = w - 1
        while c >= 0:
            times[c] = bfs(c)
            c -= 1

        return times