class UnionFind:
    def __init__(self, n):
        self.parent = []
        self.rank = []
        idx = 0
        while idx < n:
            self.parent.append(idx)
            self.rank.append(1)
            idx += 1

    def find(self, x):
        if self.parent[x] == x:
            return x
        retVal = self.find(self.parent[x])
        self.parent[x] = retVal
        return retVal

    def union(self, a, b):
        p = self.find(a)
        q = self.find(b)
        mergedFlag = False
        while not mergedFlag:
            if p != q:
                if self.rank[p] > self.rank[q]:
                    self.parent[q] = p
                    mergedFlag = True
                else:
                    if self.rank[p] < self.rank[q]:
                        self.parent[p] = q
                        mergedFlag = True
                    else:
                        self.parent[q] = p
                        self.rank[p] += 1
                        mergedFlag = True
            else:
                mergedFlag = True


class Solution:
    def minimumCost(self, n, edges, query):
        uf = UnionFind(n)
        allOnes = 1
        bitSize = 32
        maskVal = allOnes
        shiftCount = bitSize
        while shiftCount > 0:
            maskVal = maskVal * 2
            shiftCount -= 1
        maskVal -= 1

        compAnd = []
        pos = 0
        while pos < n:
            compAnd.append(maskVal)
            pos += 1

        edgePtr = 0
        while edgePtr < len(edges):
            edgeElement = edges[edgePtr]
            uVal = edgeElement[0]
            vVal = edgeElement[1]
            wVal = edgeElement[2]

            uf.union(uVal, vVal)
            findU = uf.find(uVal)
            compAnd[findU] &= wVal

            edgePtr += 1

        compCost = {}
        idxIter = 0
        while idxIter < n:
            r = uf.find(idxIter)
            if r not in compCost:
                compCost[r] = compAnd[r]
            idxIter += 1

        retList = []
        qIdx = 0
        while qIdx < len(query):
            qElem = query[qIdx]
            sVal = qElem[0]
            tVal = qElem[1]

            if sVal == tVal:
                retList.append(0)
            else:
                findS = uf.find(sVal)
                findT = uf.find(tVal)
                if findS == findT:
                    retList.append(compCost[findS])
                else:
                    retList.append(-1)
            qIdx += 1

        return retList