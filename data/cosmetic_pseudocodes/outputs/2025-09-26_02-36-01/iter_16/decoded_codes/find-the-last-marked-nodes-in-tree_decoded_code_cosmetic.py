class Solution:
    def lastMarkedNodes(self, edg):
        def dfs(w, v, h):
            for q in g[w]:
                if q != v:
                    h[q] = h[w] + 1
                    dfs(q, w, h)

        m = len(edg) + 1
        g = [[] for _ in range(m)]

        for t in edg:
            u, v = t
            g[u].append(v)
            g[v].append(u)

        d0 = [-float('inf')] * m
        d0[0] = 0
        dfs(0, -1, d0)

        a = 0
        for y in range(m):
            if d0[y] > d0[a]:
                a = y

        d1 = [-float('inf')] * m
        d1[a] = 0
        dfs(a, -1, d1)

        b = 0
        for w0 in range(m):
            if d1[w0] > d1[b]:
                b = w0

        d2 = [-float('inf')] * m
        d2[b] = 0
        dfs(b, -1, d2)

        res = []
        for idx in range(m):
            if d1[idx] > d2[idx]:
                res.append(a)
            else:
                res.append(b)

        return res