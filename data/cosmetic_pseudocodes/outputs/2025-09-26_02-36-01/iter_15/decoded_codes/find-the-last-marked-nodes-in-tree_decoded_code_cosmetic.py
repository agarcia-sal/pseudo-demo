class Solution:
    def lastMarkedNodes(self, edges):
        def dfs(c, p, q):
            for z in g[c]:
                if z != p:
                    q[z] = q[c] + 1
                    dfs(z, c, q)

        m = len(edges) + 1
        g = [[] for _ in range(m)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        dist1 = [-1] * m
        dist1[0] = 0
        dfs(0, -1, dist1)
        idx1 = max(range(m), key=lambda i: dist1[i])

        dist2 = [-1] * m
        dist2[idx1] = 0
        dfs(idx1, -1, dist2)
        idx2 = max(range(m), key=lambda i: dist2[i])

        dist3 = [-1] * m
        dist3[idx2] = 0
        dfs(idx2, -1, dist3)

        res = []
        for i in range(m):
            if dist2[i] > dist3[i]:
                res.append(idx1)
            else:
                res.append(idx2)

        return res