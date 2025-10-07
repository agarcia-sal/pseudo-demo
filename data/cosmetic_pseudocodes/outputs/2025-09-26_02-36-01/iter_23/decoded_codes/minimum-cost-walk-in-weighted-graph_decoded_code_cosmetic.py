class UnionFind:
    def __init__(self, n):
        def buildList(x, y, z, acc):
            if y > z:
                return acc
            else:
                return buildList(x, y + 1, z, acc + [y])

        def fillOnes(count, arr):
            if count == 0:
                return arr
            else:
                return fillOnes(count - 1, arr + [1])

        tempA = buildList(0, 0, n - 1, [])
        tempB = fillOnes(n, [])
        self.parent = tempA
        self.rank = tempB

    def find(self, u):
        def internalFind(x):
            if self.parent[x] == x:
                return x
            else:
                r = internalFind(self.parent[x])
                self.parent[x] = r
                return r

        return internalFind(u)

    def union(self, u, v):
        aVal = self.find(u)
        bVal = self.find(v)
        if aVal != bVal:
            if self.rank[aVal] > self.rank[bVal]:
                self.parent[bVal] = aVal
            else:
                if self.rank[aVal] < self.rank[bVal]:
                    self.parent[aVal] = bVal
                else:
                    self.parent[bVal] = aVal
                    self.rank[aVal] = self.rank[aVal] + 1


class Solution:
    def minimumCost(self, n, edges, query):
        ufVar = UnionFind(n)

        maxInt = (2 << 31) - 1  # 2**32 -1

        def initList(size, val, acc):
            if size == 0:
                return acc
            else:
                return initList(size - 1, val, acc + [val])

        compAnd = initList(n, maxInt, [])

        def processEdges(idx, arr):
            if idx >= len(arr):
                return
            else:
                triple = arr[idx]
                first = triple[0]
                second = triple[1]
                weight = triple[2]

                ufVar.union(first, second)

                rootIdx = ufVar.find(first)
                compAnd[rootIdx] = compAnd[rootIdx] & weight

                processEdges(idx + 1, arr)

        processEdges(0, edges)

        compCost = {}

        def buildCostMap(i):
            if i >= n:
                return
            else:
                r = ufVar.find(i)
                if r not in compCost:
                    compCost[r] = compAnd[r]
                buildCostMap(i + 1)

        buildCostMap(0)

        resList = []

        def processQueries(j):
            if j >= len(query):
                return
            else:
                qPair = query[j]
                leftVal = qPair[0]
                rightVal = qPair[1]

                if leftVal == rightVal:
                    # same node, cost 0
                    resList.append(0)
                else:
                    rootLeft = ufVar.find(leftVal)
                    rootRight = ufVar.find(rightVal)

                    if rootLeft == rootRight:
                        resList.append(compCost[rootLeft])
                    else:
                        resList.append(-1)
                processQueries(j + 1)

        processQueries(0)

        return resList