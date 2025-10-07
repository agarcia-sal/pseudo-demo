class UnionFind:
    def __init__(self, n):
        self.parent = []
        self.rank = []
        counter = 0
        while counter < n:
            self.parent.append(counter)
            self.rank.append(1)
            counter += 1

    def find(self, x):
        def recurse_find(y):
            if self.parent[y] == y:
                return y
            else:
                self.parent[y] = recurse_find(self.parent[y])
                return self.parent[y]
        return recurse_find(x)

    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)
        if rootA == rootB:
            return
        else:
            if not (self.rank[rootA] < self.rank[rootB]):
                if not (self.rank[rootA] > self.rank[rootB]):
                    self.parent[rootB] = rootA
                    self.rank[rootA] += 1
                else:
                    self.parent[rootB] = rootA
            else:
                self.parent[rootA] = rootB


class Solution:
    def minimumCost(self, n, edges, query):
        uf = UnionFind(n)
        mask_value = 4294967295  # 2^32 - 1
        bits_list = []
        index_counter = 0
        while index_counter < n:
            bits_list.append(mask_value)
            index_counter += 1

        for e in edges:
            uu, vv, ww = e
            uf.union(uu, vv)
            rootU = uf.find(uu)
            bits_list[rootU] &= ww

        comp_cost = {}
        for iter_i in range(n):
            root_i = uf.find(iter_i)
            if root_i not in comp_cost:
                comp_cost[root_i] = bits_list[root_i]

        ans_list = []

        def determine_answer(x, y):
            if x == y:
                return 0
            else:
                fx = uf.find(x)
                fy = uf.find(y)
                if fx == fy:
                    return comp_cost[fx]
                else:
                    return -1

        for q in query:
            ans_list.append(determine_answer(q[0], q[1]))

        return ans_list