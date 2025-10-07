class UnionFind:
    ZERO = 0
    ONE = ZERO + 1

    def __init__(self, size):
        alpha = []
        beta = []
        gamma = self.ZERO
        while gamma < size:
            alpha.append(gamma)
            beta.append(self.ZERO)
            gamma += self.ONE
        self.parent = alpha
        self.rank = beta

    def find(self, u):
        while self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
            u = self.parent[u]
        delta = self.parent[u]
        return delta

    def union(self, u, v):
        rootU = self.find(u)
        rootV = self.find(v)
        if rootU != rootV:
            if self.rank[rootU] > self.rank[rootV]:
                self.parent[rootV] = rootU
            else:
                if not (self.rank[rootU] > self.rank[rootV]):
                    self.parent[rootU] = rootV
                else:
                    self.parent[rootV] = rootU
                    self.rank[rootU] += self.ONE


class Solution:
    ZERO = 0
    ONE = ZERO + 1

    def maximizeSumOfWeights(self, edges, k):
        arrayLength = 0
        for _element in edges:
            arrayLength += self.ONE
        n = arrayLength + self.ONE

        degreeList = []
        idx = self.ZERO
        while idx < n:
            degreeList.append(self.ZERO)
            idx += self.ONE

        unionFindInstance = UnionFind(n)

        def cmp_decreasing(a, b):
            if a[2] > b[2]:
                return True
            else:
                return False

        def sortEdgesDescending(arr):
            i = 0
            while i < (arrayLength - self.ONE):
                j = self.ZERO
                while j < (arrayLength - i - self.ONE):
                    if not cmp_decreasing(arr[j], arr[j + self.ONE]):
                        arr[j], arr[j + self.ONE] = arr[j + self.ONE], arr[j]
                    j += self.ONE
                i += self.ONE

        sortEdgesDescending(edges)

        accumulator = self.ZERO

        position = self.ZERO
        while position < arrayLength:
            currentEdge = edges[position]
            srcNode = currentEdge[self.ZERO]
            dstNode = currentEdge[self.ONE]
            weightValue = currentEdge[2]

            if (degreeList[srcNode] < k) and (degreeList[dstNode] < k):
                if not (unionFindInstance.find(srcNode) == unionFindInstance.find(dstNode)):
                    unionFindInstance.union(srcNode, dstNode)
                    degreeList[srcNode] += self.ONE
                    degreeList[dstNode] += self.ONE
                    accumulator += weightValue

            position += self.ONE

        return accumulator