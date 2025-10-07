class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        x_root = self.find(u)
        y_root = self.find(v)

        if x_root != y_root:
            if self.rank[x_root] > self.rank[y_root]:
                self.parent[y_root] = x_root
            elif self.rank[x_root] < self.rank[y_root]:
                self.parent[x_root] = y_root
            else:
                self.parent[y_root] = x_root
                self.rank[x_root] += 1


class Solution:
    def minimumCost(self, n, edges, query):
        uf_instance = UnionFind(n)

        mask_limit = (1 << 32) - 1
        comp_mask = [mask_limit] * n

        for a, b, c in edges:
            uf_instance.union(a, b)
            root_idx = uf_instance.find(a)
            comp_mask[root_idx] &= c

        costs_map = {}
        for i in range(n):
            root_val = uf_instance.find(i)
            if root_val not in costs_map:
                costs_map[root_val] = comp_mask[root_val]

        res_list = []
        for first_val, second_val in query:
            if first_val == second_val:
                res_list.append(0)
            else:
                root_first = uf_instance.find(first_val)
                root_second = uf_instance.find(second_val)
                if root_first == root_second:
                    res_list.append(costs_map[root_first])
                else:
                    res_list.append(-1)

        return res_list