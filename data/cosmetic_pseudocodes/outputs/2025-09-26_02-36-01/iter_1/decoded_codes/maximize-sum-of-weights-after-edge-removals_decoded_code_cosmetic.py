class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, u):
        while self.parent[u] != u:
            self.parent[u] = self.parent[self.parent[u]]  # Path compression
            u = self.parent[u]
        return u

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u == root_v:
            return

        if self.rank[root_u] < self.rank[root_v]:
            self.parent[root_u] = root_v
        elif self.rank[root_v] < self.rank[root_u]:
            self.parent[root_v] = root_u
        else:
            self.parent[root_v] = root_u
            self.rank[root_u] += 1


class Solution:
    def maximizeSumOfWeights(self, edges, k):
        node_count = len(edges) + 1
        degree_list = [0] * node_count
        uf_instance = UnionFind(node_count)

        # Sort edges in descending order of weight
        edges.sort(key=lambda edge: edge[2], reverse=True)

        total_weight = 0

        for node_u, node_v, weight in edges:
            if degree_list[node_u] < k and degree_list[node_v] < k and uf_instance.find(node_u) != uf_instance.find(node_v):
                uf_instance.union(node_u, node_v)
                degree_list[node_u] += 1
                degree_list[node_v] += 1
                total_weight += weight

        return total_weight