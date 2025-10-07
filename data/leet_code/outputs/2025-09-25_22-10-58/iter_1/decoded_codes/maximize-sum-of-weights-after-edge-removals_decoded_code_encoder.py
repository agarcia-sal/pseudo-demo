from typing import List

class UnionFind:
    def __init__(self, size: int):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, u: int) -> int:
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u: int, v: int):
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
    def maximizeSumOfWeights(self, edges: List[List[int]], k: int) -> int:
        n = len(edges) + 1
        degree = [0] * n
        uf = UnionFind(n)

        edges.sort(key=lambda x: x[2], reverse=True)

        max_sum = 0

        for u, v, w in edges:
            if degree[u] < k and degree[v] < k and uf.find(u) != uf.find(v):
                uf.union(u, v)
                degree[u] += 1
                degree[v] += 1
                max_sum += w

        return max_sum