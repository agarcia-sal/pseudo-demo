class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
            x = self.parent[x]
        return x

    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)
        if rootA != rootB:
            if self.rank[rootA] > self.rank[rootB]:
                self.parent[rootB] = rootA
            elif self.rank[rootA] < self.rank[rootB]:
                self.parent[rootA] = rootB
            else:
                self.parent[rootB] = rootA
                self.rank[rootA] += 1


class Solution:
    def minimumCost(self, n, edges, query):
        uf = UnionFind(n)
        max_mask = (1 << 32) - 1
        comp_mask = [max_mask] * n

        for node1, node2, weight in edges:
            uf.union(node1, node2)
            leader = uf.find(node1)
            comp_mask[leader] &= weight

        comp_cost_map = {}
        for i in range(n):
            group_leader = uf.find(i)
            if group_leader not in comp_cost_map:
                comp_cost_map[group_leader] = comp_mask[group_leader]

        response_list = []
        for start_node, end_node in query:
            if start_node == end_node:
                response_list.append(0)
            elif uf.find(start_node) == uf.find(end_node):
                response_list.append(comp_cost_map[uf.find(start_node)])
            else:
                response_list.append(-1)

        return response_list