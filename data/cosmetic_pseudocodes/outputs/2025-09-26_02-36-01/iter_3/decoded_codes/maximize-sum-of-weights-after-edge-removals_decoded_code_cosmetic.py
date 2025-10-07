from typing import List, Tuple

class UnionFind:
    def __init__(self, size: int):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, u: int) -> int:
        while self.parent[u] != u:
            self.parent[u] = self.parent[self.parent[u]]
            u = self.parent[u]
        return u

    def union(self, u: int, v: int) -> None:
        rootU = self.find(u)
        rootV = self.find(v)
        if rootU != rootV:
            if self.rank[rootU] > self.rank[rootV]:
                self.parent[rootV] = rootU
            elif self.rank[rootU] < self.rank[rootV]:
                self.parent[rootU] = rootV
            else:
                self.parent[rootV] = rootU
                self.rank[rootU] += 1

class Solution:
    def maximizeSumOfWeights(self, edges: List[Tuple[int, int, int]], k: int) -> int:
        countNodes = len(edges) + 1
        deg = [0] * countNodes
        uf = UnionFind(countNodes)
        edges = sorted(edges, key=lambda edge: -edge[2])
        totalWeight = 0
        idx = 0
        while idx < len(edges):
            n1, n2, weight = edges[idx]
            if deg[n1] < k and deg[n2] < k:
                if uf.find(n1) != uf.find(n2):
                    uf.union(n1, n2)
                    deg[n1] += 1
                    deg[n2] += 1
                    totalWeight += weight
            idx += 1
        return totalWeight