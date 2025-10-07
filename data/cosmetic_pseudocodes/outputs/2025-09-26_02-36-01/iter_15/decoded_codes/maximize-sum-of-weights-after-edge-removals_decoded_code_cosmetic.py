from typing import List

class UnionFind:
    def __init__(self, size: int):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, u: int) -> int:
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u: int, v: int) -> None:
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] == self.rank[root_v]:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            else:
                self.parent[root_u] = root_v

class Solution:
    def maximizeSumOfWeights(self, edges: List[List[int]], k: int) -> int:
        n = len(edges) + 1
        degree = [0] * n

        uf = UnionFind(n)

        # Sort edges descending by weight
        edges.sort(key=lambda x: x[2], reverse=True)

        max_sum = 0
        for u, v, w in edges:
            if degree[u] < k and degree[v] < k and uf.find(u) != uf.find(v):
                uf.union(u, v)
                degree[u] += 1
                degree[v] += 1
                max_sum += w

        return max_sum