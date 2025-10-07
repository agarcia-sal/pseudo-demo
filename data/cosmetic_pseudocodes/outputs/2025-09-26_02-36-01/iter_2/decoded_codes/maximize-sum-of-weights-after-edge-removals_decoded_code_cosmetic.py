from typing import List, Tuple

class UnionFind:
    def __init__(self, length: int):
        self.parent = [i for i in range(length)]
        self.rank = [0] * length

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> None:
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            if self.rank[root_a] > self.rank[root_b]:
                self.parent[root_b] = root_a
            elif self.rank[root_a] < self.rank[root_b]:
                self.parent[root_a] = root_b
            else:
                self.parent[root_b] = root_a
                self.rank[root_a] += 1

class Solution:
    def maximizeSumOfWeights(self, edges: List[Tuple[int, int, int]], limit: int) -> int:
        total_nodes = len(edges) + 1
        degree_counter = [0] * total_nodes
        union_find = UnionFind(total_nodes)

        ordered_edges = sorted(edges, key=lambda e: e[2], reverse=True)

        accumulated_sum = 0
        idx = 0
        while idx < len(ordered_edges):
            current_edge = ordered_edges[idx]
            start_node, end_node, weight = current_edge

            if degree_counter[start_node] < limit and degree_counter[end_node] < limit:
                root_start = union_find.find(start_node)
                root_end = union_find.find(end_node)
                if root_start != root_end:
                    union_find.union(start_node, end_node)
                    degree_counter[start_node] += 1
                    degree_counter[end_node] += 1
                    accumulated_sum += weight
            idx += 1

        return accumulated_sum