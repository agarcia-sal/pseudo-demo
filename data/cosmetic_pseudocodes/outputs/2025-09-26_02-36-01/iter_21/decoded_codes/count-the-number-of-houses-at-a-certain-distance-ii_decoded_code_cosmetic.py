class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> list[int]:
        if not (x <= y):
            x, y = y, x

        def bfs(start: int) -> list[int]:
            # Initialize boolean visited list and distance list
            vsd = [False] * (n + 1)
            dist = [0] * (n + 1)

            que = [start]
            vsd[start] = True

            while len(que) > 0:
                cur = que.pop(0)

                for adj in (cur - 1, cur + 1):
                    if 1 <= adj <= n and not vsd[adj]:
                        vsd[adj] = True
                        dist[adj] = dist[cur] + 1
                        que.append(adj)

                if cur == x and not vsd[y]:
                    vsd[y] = True
                    dist[y] = dist[cur] + 1
                    que.append(y)
                elif cur == y and not vsd[x]:
                    vsd[x] = True
                    dist[x] = dist[cur] + 1
                    que.append(x)

            return dist[1:]

        wrt = [0] * n

        zmd = 1
        while zmd <= n:
            dists = bfs(zmd)
            for val in dists:
                if val > 0:
                    wrt[val - 1] += 1
            zmd += 1

        return wrt