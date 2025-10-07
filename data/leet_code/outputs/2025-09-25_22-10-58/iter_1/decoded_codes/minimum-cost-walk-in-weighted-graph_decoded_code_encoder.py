class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        rootU = self.find(u)
        rootV = self.find(v)
        if rootU != rootV:
            if self.rank[rootU] > self.rank[rootV]:
                self.parent[rootV] = rootU
            elif self.rank[rootU] < self.rank[rootV]:
                self.parent[rootU] = rootV
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
        for i in range(n):
            root = uf.find(i)
            if root not in component_cost:
                component_cost[root] = component_and[root]

        result = []
        for s, t in query:
            if s == t:
                result.append(0)
            else:
                rootS = uf.find(s)
                rootT = uf.find(t)
                if rootS == rootT:
                    result.append(component_cost[rootS])
                else:
                    result.append(-1)

        return result