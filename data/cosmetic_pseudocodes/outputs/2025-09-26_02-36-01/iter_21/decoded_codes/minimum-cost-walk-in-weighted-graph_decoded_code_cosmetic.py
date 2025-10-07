class UnionFind:
    def __init__(self, n):
        self.parent = []
        self.rank = []
        for z in range(n):
            self.parent.append(z)
            self.rank.append(1)

    def find(self, a):
        def innerFind(x):
            if self.parent[x] != x:
                temp = innerFind(self.parent[x])
                self.parent[x] = temp
                return temp
            else:
                return self.parent[x]
        return innerFind(a)

    def union(self, b, c):
        root1 = self.find(b)
        root2 = self.find(c)
        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1


class Solution:
    def minimumCost(self, p, q, r):
        uf = UnionFind(p)

        def powEquivalent():
            return (1 << 32) - 1

        compData = [powEquivalent() for _ in range(p)]

        def updateComp(arr):
            idx = uf.find(arr[0])
            compData[idx] &= arr[2]

        for edge in r:
            updateComp(edge)
            uf.union(edge[0], edge[1])

        compCosts = {}
        for i in range(p):
            rootNode = uf.find(i)
            if rootNode not in compCosts:
                compCosts[rootNode] = compData[rootNode]

        ansList = []

        def processQueries(sVal, tVal):
            if sVal == tVal:
                ansList.append(0)
            else:
                rootS = uf.find(sVal)
                rootT = uf.find(tVal)
                if rootS == rootT:
                    ansList.append(compCosts[rootS])
                else:
                    ansList.append(-1)

        for query in q:
            processQueries(query[0], query[1])

        return ansList