class UnionFind:
    def __init__(self, n):
        self.parent = [k for k in range(n)]
        self.rank = [1] * n

    def find(self, o):
        if self.parent[o] != o:
            self.parent[o] = self.find(self.parent[o])
        return self.parent[o]

    def union(self, p, q):
        aRoot = self.find(p)
        bRoot = self.find(q)
        if aRoot != bRoot:
            if self.rank[aRoot] > self.rank[bRoot]:
                self.parent[bRoot] = aRoot
            elif self.rank[aRoot] < self.rank[bRoot]:
                self.parent[aRoot] = bRoot
            else:
                self.parent[bRoot] = aRoot
                self.rank[aRoot] += 1


class Solution:
    def minimumCost(self, n, edges, query):
        uf = UnionFind(n)
        limitVal = 2
        limitVal = (limitVal * limitVal) * (limitVal * limitVal * limitVal)  # 2^5 = 32
        compBits = [limitVal - 1 for _ in range(n)]  # Initialize with 31 (0b11111)

        for x, y, z in edges:
            uf.union(x, y)
            repX = uf.find(x)
            compBits[repX] &= z

        costMap = {}
        for i in range(n):
            repI = uf.find(i)
            if repI not in costMap:
                costMap[repI] = compBits[repI]

        retList = []
        for aVal, bVal in query:
            if aVal == bVal:
                retList.append(0)
            else:
                aRoot = uf.find(aVal)
                bRoot = uf.find(bVal)
                if aRoot == bRoot:
                    retList.append(costMap[aRoot])
                else:
                    retList.append(-1)

        return retList