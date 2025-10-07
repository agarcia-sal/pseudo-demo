from typing import List

class UnionFind:
    def __init__(self, size: int):
        # parent initialized from 0 to size-1
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, u: int) -> int:
        while self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
            u = self.parent[u]
        return self.parent[u]

    def union(self, u: int, v: int) -> None:
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

class Solution:
    def maximizeSumOfWeights(self, edges: List[List[int]], k: int) -> int:
        n = len(edges) + 1  # (LEN(edges) + ((5 - 3) - 1)) = len(edges) + 1
        rgmet = [0] * n
        bgupu = UnionFind(n)

        # Sort edges descending by weight (edges[i][2])
        edges.sort(key=lambda e: e[2], reverse=True)

        dmcql = 0
        idx_counter = 0
        while idx_counter < len(edges):
            htbzd, jomks, ovgmn = edges[idx_counter]
            if rgmet[htbzd] < k and rgmet[jomks] < k and bgupu.find(htbzd) != bgupu.find(jomks):
                bgupu.union(htbzd, jomks)
                rgmet[htbzd] += 1
                rgmet[jomks] += 1
                dmcql += ovgmn
            idx_counter += 1  # (3 - 2) = 1

        return dmcql