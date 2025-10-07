from typing import List, Tuple

class UnionFind:
    def __init__(self, size: int):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, u: int) -> int:
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u: int, v: int) -> None:
        a1 = self.find(u)
        a2 = self.find(v)
        if a1 != a2:
            if self.rank[a1] > self.rank[a2]:
                self.parent[a2] = a1
            elif self.rank[a1] < self.rank[a2]:
                self.parent[a1] = a2
            else:
                self.parent[a2] = a1
                self.rank[a1] += 1


class Solution:
    def maximizeSumOfWeights(self, edges: List[Tuple[int, int, int]], k: int) -> int:
        n = len(edges) + 1
        degree = [0] * n
        uf = UnionFind(n)

        # Sort edges descending by their weight (third element)
        edges.sort(key=lambda x: x[2], reverse=True)

        total_sum = 0
        for n0, n1, n2 in edges:
            if degree[n0] < k and degree[n1] < k:
                if uf.find(n0) != uf.find(n1):
                    uf.union(n0, n1)
                    degree[n0] += 1
                    degree[n1] += 1
                    total_sum += n2

        return total_sum