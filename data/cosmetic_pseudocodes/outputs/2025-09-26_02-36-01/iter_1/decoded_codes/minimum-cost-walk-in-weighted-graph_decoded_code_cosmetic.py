class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, u):
        while u != self.parent[u]:
            self.parent[u] = self.parent[self.parent[u]]  # Path compression by halving
            u = self.parent[u]
        return u

    def union(self, u, v):
        rootU = self.find(u)
        rootV = self.find(v)
        if rootU != rootV:
            if self.rank[rootU] < self.rank[rootV]:
                self.parent[rootU] = rootV
            elif self.rank[rootU] > self.rank[rootV]:
                self.parent[rootV] = rootU
            else:
                self.parent[rootV] = rootU
                self.rank[rootU] += 1


class Solution:
    def minimumCost(self, n, edges, query):
        uf = UnionFind(n)
        component_and = [(1 << 32) - 1] * n

        for u, v, w in edges:
            uf.union(u, v)
            root = uf.find(u)
            component_and[root] &= w

        component_cost = {}
        for index in range(n):
            root = uf.find(index)
            if root not in component_cost:
                component_cost[root] = component_and[root]

        results = []
        for s, t in query:
            if s == t:
                results.append(0)
            elif uf.find(s) == uf.find(t):
                results.append(component_cost[uf.find(s)])
            else:
                results.append(-1)

        return results