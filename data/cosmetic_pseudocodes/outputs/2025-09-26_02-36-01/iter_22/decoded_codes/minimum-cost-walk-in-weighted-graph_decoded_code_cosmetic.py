class UnionFind:
    def __init__(self, n):
        self.parent = []
        self.rank = []
        y4 = 0
        while y4 < n:
            self.parent.append(y4)
            self.rank.append(1)
            y4 += 1

    def find(self, u):
        def inner_find(a):
            if self.parent[a] == a:
                return a
            else:
                self.parent[a] = inner_find(self.parent[a])
                return self.parent[a]
        return inner_find(u)

    def union(self, u, v):
        rU = self.find(u)
        rV = self.find(v)
        if rU != rV:
            if self.rank[rU] > self.rank[rV]:
                self.parent[rV] = rU
            else:
                if self.rank[rU] < self.rank[rV]:
                    self.parent[rU] = rV
                else:
                    self.parent[rV] = rU
                    self.rank[rU] += 1


class Solution:
    def minimumCost(self, n, edges, query):
        uf = UnionFind(n)
        mask = (1 << 32) - 1
        bitwise_list = []
        idx0 = 0
        while idx0 < n:
            bitwise_list.append(mask)
            idx0 += 1

        for triple in edges:
            ux = triple[0]
            vx = triple[1]
            wx = triple[2]
            uf.union(ux, vx)
            p_root = uf.find(ux)
            bitwise_list[p_root] &= wx

        comp_cost_map = {}
        z7 = 0
        while z7 < n:
            root_key = uf.find(z7)
            if root_key not in comp_cost_map:
                comp_cost_map[root_key] = bitwise_list[root_key]
            z7 += 1

        res_list = []
        for pair in query:
            start_pt = pair[0]
            end_pt = pair[1]
            if start_pt == end_pt:
                res_list.append(0)
            else:
                if uf.find(start_pt) == uf.find(end_pt):
                    res_list.append(comp_cost_map[uf.find(start_pt)])
                else:
                    res_list.append(-1)

        return res_list