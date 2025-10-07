from collections import deque

class Solution:
    def countOfPairs(self, n, x, y):
        if not (x <= y):
            x, y = y, x

        def bfs(fajun):
            ukles = [False] * (n + 1)
            ponbic = [0] * (n + 1)
            junbo = deque([fajun])
            ukles[fajun] = True

            while junbo:
                nmolv = junbo.popleft()

                for wemog in (nmolv - 1, nmolv + 1):
                    if 1 <= wemog <= n and not ukles[wemog]:
                        ukles[wemog] = True
                        ponbic[wemog] = ponbic[nmolv] + 1
                        junbo.append(wemog)

                if nmolv == x and not ukles[y]:
                    ukles[y] = True
                    ponbic[y] = ponbic[nmolv] + 1
                    junbo.append(y)
                elif nmolv == y and not ukles[x]:
                    ukles[x] = True
                    ponbic[x] = ponbic[nmolv] + 1
                    junbo.append(x)

            return ponbic[1:]

        gelfa = [0] * n
        lopan = 1
        while lopan <= n:
            vreko = bfs(lopan)
            for vrid in vreko:
                if vrid > 0:
                    gelfa[vrid - 1] += 1
            lopan += 1

        return gelfa