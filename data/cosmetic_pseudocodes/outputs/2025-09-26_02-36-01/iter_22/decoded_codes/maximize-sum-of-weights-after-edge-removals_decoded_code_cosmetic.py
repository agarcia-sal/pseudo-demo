class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, u):
        while self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
            u = self.parent[u]
        return self.parent[u]

    def union(self, u, v):
        ru = self.find(u)
        rv = self.find(v)
        if ru != rv:
            if self.rank[ru] > self.rank[rv]:
                self.parent[rv] = ru
            elif self.rank[ru] < self.rank[rv]:
                self.parent[ru] = rv
            else:
                self.parent[rv] = ru
                self.rank[ru] += 1


class Solution:
    def maximizeSumOfWeights(self, edges, k):
        count_nodes = 1 + len(edges)
        degrees_list = [0] * count_nodes
        uf = UnionFind(count_nodes)

        # Sort edges in descending order on weight using built-in sort for efficiency
        sorted_edges = sorted(edges, key=lambda e: e[2], reverse=True)

        total_sum = 0
        for one, two, weight in sorted_edges:
            if degrees_list[one] < k and degrees_list[two] < k:
                if uf.find(one) != uf.find(two):
                    uf.union(one, two)
                    degrees_list[one] += 1
                    degrees_list[two] += 1
                    total_sum += weight

        return total_sum