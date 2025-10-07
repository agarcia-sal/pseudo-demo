class UnionFind:
    def __init__(self, size):
        a = 0
        b = size - 1
        self.parent = []
        self.rank = []
        while a <= b:
            self.parent.append(a)
            self.rank.append(0)
            a += 1

    def find(self, u):
        val = self.parent[u]
        if val != u:
            res = self.find(val)
            self.parent[u] = res
        return self.parent[u]

    def union(self, u, v):
        p = self.find(u)
        q = self.find(v)
        if p != q:
            if self.rank[p] > self.rank[q]:
                self.parent[q] = p
            else:
                if self.rank[p] < self.rank[q]:
                    self.parent[p] = q
                else:
                    self.parent[q] = p
                    self.rank[p] += 1


class Solution:
    def maximizeSumOfWeights(self, edges, k):
        totalCount = len(edges) + 1
        counts = [0] * totalCount
        unionFindInstance = UnionFind(totalCount)
        currentSum = 0

        # Sort edges descending by weight (edges[i][2])
        edges.sort(key=lambda x: x[2], reverse=True)

        idx = 0
        while idx < len(edges):
            edgeU, edgeV, edgeW = edges[idx]
            canConnect = (
                counts[edgeU] < k and
                counts[edgeV] < k and
                unionFindInstance.find(edgeU) != unionFindInstance.find(edgeV)
            )
            if canConnect:
                unionFindInstance.union(edgeU, edgeV)
                counts[edgeU] += 1
                counts[edgeV] += 1
                currentSum += edgeW
            idx += 1

        return currentSum