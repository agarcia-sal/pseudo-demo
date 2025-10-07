from typing import List, Tuple

class UnionFind:
    def __init__(self, size: int):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, u: int) -> int:
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

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
        total_nodes = len(edges) + 1
        deg_list = [0] * total_nodes
        uf = UnionFind(total_nodes)

        temp_edges = sorted(edges, key=lambda x: x[2], reverse=True)

        maxSum = 0
        pointer = 0
        count_edges = len(temp_edges)

        while pointer < count_edges:
            current_edge = temp_edges[pointer]
            nodeA, nodeB, weight = current_edge

            if deg_list[nodeA] < k and deg_list[nodeB] < k and uf.find(nodeA) != uf.find(nodeB):
                uf.union(nodeA, nodeB)
                deg_list[nodeA] += 1
                deg_list[nodeB] += 1
                maxSum += weight

            pointer += 1

        return maxSum