from typing import List

class UnionFind:
    def __init__(self, size: int):
        # Initialize parent to self and rank to 0 for all elements
        self.parent = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, u: int) -> int:
        # Path compression helper function
        def helper(x: int) -> int:
            if self.parent[x] == x:
                return x
            self.parent[x] = helper(self.parent[x])
            return self.parent[x]
        return helper(u)

    def union(self, u: int, v: int) -> None:
        rootU = self.find(u)
        rootV = self.find(v)
        if rootU != rootV:
            rankU = self.rank[rootU]
            rankV = self.rank[rootV]
            if rankU > rankV:
                self.parent[rootV] = rootU
            elif rankU < rankV:
                self.parent[rootU] = rootV
            else:
                self.parent[rootV] = rootU
                self.rank[rootU] += 1

class Solution:
    def maximizeSumOfWeights(self, edges: List[List[int]], k: int) -> int:
        n = len(edges) + 1
        degrees = [0] * n
        uf = UnionFind(n)

        # Sort edges by descending weight (manual sort as in pseudocode)
        sortedEdges = []
        edges_copy = edges[:]  # To avoid modifying original input
        while edges_copy:
            max_index = 0
            for idx in range(len(edges_copy)):
                if edges_copy[idx][2] > edges_copy[max_index][2]:
                    max_index = idx
            sortedEdges.append(edges_copy[max_index])
            edges_copy.pop(max_index)

        maximumSum = 0

        def processEdge(i: int) -> None:
            nonlocal maximumSum
            if i == len(sortedEdges):
                return
            u, v, w = sortedEdges[i]
            if degrees[u] < k and degrees[v] < k and uf.find(u) != uf.find(v):
                uf.union(u, v)
                degrees[u] += 1
                degrees[v] += 1
                maximumSum += w
            processEdge(i + 1)

        processEdge(0)
        return maximumSum