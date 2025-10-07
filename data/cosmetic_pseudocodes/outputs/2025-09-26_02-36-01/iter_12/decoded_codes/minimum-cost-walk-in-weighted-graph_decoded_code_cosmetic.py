class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]

    def find(self, u):
        def recurse(x):
            if self.parent[x] != x:
                self.parent[x] = recurse(self.parent[x])
            return self.parent[x]
        return recurse(u)

    def union(self, u, v):
        rootX = self.find(u)
        rootY = self.find(v)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            else:
                if self.rank[rootX] < self.rank[rootY]:
                    self.parent[rootX] = rootY
                else:
                    self.parent[rootY] = rootX
                    self.rank[rootX] += 1


class Solution:
    def minimumCost(self, n, edges, query):
        uf = UnionFind(n)
        maskVal = (1 << 32) - 1

        compAnd = [maskVal for _ in range(n)]

        for u, v, w in edges:
            uf.union(u, v)
            compIndex = uf.find(u)
            compAnd[compIndex] &= w

        compCost = {}
        for i in range(n):
            rootVal = uf.find(i)
            if rootVal not in compCost:
                compCost[rootVal] = compAnd[rootVal]

        resultList = []

        def processPair(pair):
            sVal, tVal = pair
            if sVal == tVal:
                return 0
            else:
                rootS = uf.find(sVal)
                rootT = uf.find(tVal)
                if rootS == rootT:
                    return compCost[rootS]
                else:
                    return -1

        for pairVal in query:
            resultList.append(processPair(pairVal))

        return resultList