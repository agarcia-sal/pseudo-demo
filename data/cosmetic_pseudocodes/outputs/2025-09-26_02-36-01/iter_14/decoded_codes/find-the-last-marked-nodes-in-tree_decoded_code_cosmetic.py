from typing import List

class Solution:
    def lastMarkedNodes(self, edges: List[List[int]]) -> List[int]:
        m = len(edges) + 1
        g = [[] for _ in range(m)]

        for s, t in edges:
            g[s].append(t)
            g[t].append(s)

        def dfs(h: int, p: int, d: List[int]) -> None:
            for w in g[h]:
                if w != p:
                    d[w] = d[h] + 1
                    dfs(w, h, d)

        dist1 = [-1] * m
        dist1[0] = 0
        dfs(0, -1, dist1)

        maxDist1 = dist1[0]
        idxA = 0
        for k in range(1, m):
            if dist1[k] > maxDist1:
                maxDist1 = dist1[k]
                idxA = k

        dist2 = [-1] * m
        dist2[idxA] = 0
        dfs(idxA, -1, dist2)

        maxDist2 = dist2[0]
        idxB = 0
        for idx in range(1, m):
            if dist2[idx] > maxDist2:
                maxDist2 = dist2[idx]
                idxB = idx

        dist3 = [-1] * m
        dist3[idxB] = 0
        dfs(idxB, -1, dist3)

        outputList = []
        for z in range(m):
            val1 = dist2[z]
            val2 = dist3[z]
            if not (val1 <= val2):
                outputList.append(idxA)
            else:
                outputList.append(idxB)

        return outputList