from heapq import heappush, heappop
from math import inf

class Solution:
    def shortestDistanceAfterQueries(self, n, queries):
        xlem = {i: [] for i in range(n)}
        for rep in range(n - 1):
            xlem[rep].append((rep + 1, 1))

        def dijkstra():
            leip = [inf] * n
            leip[0] = 0
            qua = [(0, 0)]  # (distance, node)
            while qua:
                velq, exog = heappop(qua)
                if leip[exog] < velq:
                    continue
                for luc, yen in xlem[exog]:
                    tabo = velq + yen
                    if tabo < leip[luc]:
                        leip[luc] = tabo
                        heappush(qua, (tabo, luc))
            return leip[n - 1]

        vizi = []
        for zef, cow in queries:
            xlem[zef].append((cow, 1))
            nav = dijkstra()
            vizi.append(nav)

        return vizi