from typing import List

class Solution:
    def lastMarkedNodes(self, edges: List[List[int]]) -> List[int]:
        def dfs(k: int, p: int, r: List[int]) -> None:
            m = len(g[k])
            q = 0
            while q < m:
                s = g[k][q]
                if s != p:
                    r[s] = r[k] + 1
                    dfs(s, k, r)
                q += 1

        o = len(edges)
        g = []
        v = 0
        while True:
            if v > o:
                break
            g.append([])
            v += 1

        for c, d in edges:
            g[c].append(d)
            g[d].append(c)

        dist1 = []
        x = 0
        while True:
            if x > o:
                break
            dist1.append(-1)
            x += 1
        dist1[0] = 0
        dfs(0, -1, dist1)

        a = 0
        y = 1
        while y < len(dist1):
            if dist1[y] > dist1[a]:
                a = y
            y += 1

        dist2 = []
        z = 0
        while True:
            if z > o:
                break
            dist2.append(-1)
            z += 1
        dist2[a] = 0
        dfs(a, -1, dist2)

        b = 0
        w = 1
        while w < len(dist2):
            if dist2[w] > dist2[b]:
                b = w
            w += 1

        dist3 = []
        r_ = 0
        while True:
            if r_ > o:
                break
            dist3.append(-1)
            r_ += 1
        dist3[b] = 0
        dfs(b, -1, dist3)

        result = []
        i = 0
        while i < len(dist2):
            if dist2[i] > dist3[i]:
                result.append(a)
            else:
                result.append(b)
            i += 1

        return result