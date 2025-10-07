from collections import deque

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> list[int]:
        wv = [0] * n

        def bfs(start: int):
            hh = [False] * (n + 1)
            dd = [0] * (n + 1)
            qq = deque([start])
            hh[start] = True

            while qq:
                vv = qq.popleft()

                for uu in (vv - 1, vv + 1):
                    if 1 <= uu <= n and not hh[uu]:
                        hh[uu] = True
                        dd[uu] = dd[vv] + 1
                        qq.append(uu)

                if vv == x and not hh[y]:
                    hh[y] = True
                    dd[y] = dd[vv] + 1
                    qq.append(y)

                if vv == y and not hh[x]:
                    hh[x] = True
                    dd[x] = dd[vv] + 1
                    qq.append(x)

            for jj in range(1, n + 1):
                if dd[jj] > 0:
                    wv[dd[jj] - 1] += 1

        for zz in range(1, n + 1):
            bfs(zz)

        return wv