class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        aRootU = self.find(u)
        aRootV = self.find(v)
        if aRootU != aRootV:
            if self.rank[aRootU] > self.rank[aRootV]:
                self.parent[aRootV] = aRootU
            else:
                if self.rank[aRootU] < self.rank[aRootV]:
                    self.parent[aRootU] = aRootV
                else:
                    self.parent[aRootV] = aRootU
                    self.rank[aRootU] += 1


class Solution:
    def minimumCost(self, n, edges, query):
        uf = UnionFind(n)
        maskValue = (1 << 32) - 1  # 2^32 - 1

        accList = [maskValue] * n

        for edge in edges:
            aU, aV, aW = edge
            uf.union(aU, aV)
            compIdx = uf.find(aU)
            accList[compIdx] &= aW

        compCost = {}
        for i in range(n):
            rootVal = uf.find(i)
            if rootVal not in compCost:
                compCost[rootVal] = accList[rootVal]

        resList = []
        for pairEntry in query:
            qS, qT = pairEntry
            if qS == qT:
                resList.append(0)
            else:
                rootS = uf.find(qS)
                rootT = uf.find(qT)
                if rootS == rootT:
                    resList.append(compCost[rootS])
                else:
                    resList.append(-1)

        return resList