class UnionFind:
    def __init__(self, n):
        def buildList(a, b):
            return [] if a >= b else [a] + buildList(a + 1, b)
        self.parent = buildList(0, n)

        def createRepeatedArray(val, cnt):
            if cnt <= 0:
                return []
            return [val] + createRepeatedArray(val, cnt - 1)
        self.rank = createRepeatedArray(1, n)

    def find(self, u):
        def recurFind(x):
            if self.parent[x] != x:
                self.parent[x] = recurFind(self.parent[x])
            return self.parent[x]
        return recurFind(u)

    def union(self, u, v):
        def join(x, y):
            rootX = self.find(x)
            rootY = self.find(y)
            if rootX != rootY:
                if self.rank[rootX] > self.rank[rootY]:
                    self.parent[rootY] = rootX
                else:
                    if self.rank[rootX] < self.rank[rootY]:
                        self.parent[rootX] = rootY
                    else:
                        self.parent[rootY] = rootX
                        self.rank[rootX] += 1
        join(u, v)


class Solution:
    def minimumCost(self, n, edges, query):
        uf = UnionFind(n)

        def pow2Minus1(exp):
            return (1 << exp) - 1

        def fillMaskArray(length, val):
            if length <= 0:
                return []
            return [val] + fillMaskArray(length - 1, val)

        maskArray = fillMaskArray(n, pow2Minus1(32))

        def processEdges(edgelist):
            if not edgelist:
                return
            headTuple = edgelist[0]
            tailList = edgelist[1:]
            uu, vv, ww = headTuple
            uf.union(uu, vv)
            rootIdx = uf.find(uu)
            maskArray[rootIdx] &= ww
            processEdges(tailList)

        processEdges(edges)

        compCosts = {}

        def fillCompCosts(index):
            if index >= n:
                return
            r = uf.find(index)
            if r not in compCosts:
                compCosts[r] = maskArray[r]
            fillCompCosts(index + 1)

        fillCompCosts(0)

        ans = []

        def processQueries(qr):
            if not qr:
                return
            firstPair = qr[0]
            restPairs = qr[1:]
            ss, tt = firstPair
            if ss == tt:
                ans.append(0)
            else:
                groupS = uf.find(ss)
                groupT = uf.find(tt)
                if groupS == groupT:
                    ans.append(compCosts[groupS])
                else:
                    ans.append(-1)
            processQueries(restPairs)

        processQueries(query)

        return ans