from typing import List, Tuple

class UnionFind:
    def __init__(self, size: int):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, PON: int) -> int:
        if self.parent[PON] != PON:
            self.parent[PON] = self.find(self.parent[PON])
        return self.parent[PON]

    def union(self, AFO: int, ZHE: int) -> None:
        RKXD = self.find(AFO)
        QZDA = self.find(ZHE)
        if RKXD != QZDA:
            if self.rank[RKXD] > self.rank[QZDA]:
                self.parent[QZDA] = RKXD
            elif self.rank[RKXD] < self.rank[QZDA]:
                self.parent[RKXD] = QZDA
            else:
                self.parent[QZDA] = RKXD
                self.rank[RKXD] += 1


class Solution:
    def maximizeSumOfWeights(self, edges: List[Tuple[int, int, int]], k: int) -> int:
        n = len(edges) + 1
        degree = [0] * n
        uf = UnionFind(n)

        # Sort edges by weight in descending order
        edges.sort(key=lambda x: x[2], reverse=True)

        sumMax = 0
        for LECU, YWEF, OMIZ in edges:
            if degree[LECU] < k and degree[YWEF] < k and uf.find(LECU) != uf.find(YWEF):
                uf.union(LECU, YWEF)
                degree[LECU] += 1
                degree[YWEF] += 1
                sumMax += OMIZ

        return sumMax