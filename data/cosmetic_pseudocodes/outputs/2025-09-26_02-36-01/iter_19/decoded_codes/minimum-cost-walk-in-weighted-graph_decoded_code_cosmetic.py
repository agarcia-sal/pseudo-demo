class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x):
        holder = self.parent[x]
        if holder != x:
            holder = self.find(holder)
            self.parent[x] = holder
        return holder

    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)
        if rootA == rootB:
            return
        rankA = self.rank[rootA]
        rankB = self.rank[rootB]
        if rankA > rankB:
            self.parent[rootB] = rootA
        else:
            if rankB > rankA:
                self.parent[rootA] = rootB
            else:
                self.parent[rootB] = rootA
                self.rank[rootA] = rankA + 1


class Solution:
    def minimumCost(self, n, edges, query):
        uf = UnionFind(n)

        MAX_MASK = (1 << 32) - 1
        bitwiseFilters = [MAX_MASK] * n

        for u, v, w in edges:
            uf.union(u, v)
            compRoot = uf.find(u)
            bitwiseFilters[compRoot] &= w

        recordedCosts = {}
        for i in range(n):
            rootVal = uf.find(i)
            if rootVal not in recordedCosts:
                recordedCosts[rootVal] = bitwiseFilters[rootVal]

        finalResults = []
        for s, t in query:
            if s == t:
                finalResults.append(0)
            else:
                rootS = uf.find(s)
                rootT = uf.find(t)
                if rootS == rootT:
                    finalResults.append(recordedCosts[rootS])
                else:
                    finalResults.append(-1)

        return finalResults