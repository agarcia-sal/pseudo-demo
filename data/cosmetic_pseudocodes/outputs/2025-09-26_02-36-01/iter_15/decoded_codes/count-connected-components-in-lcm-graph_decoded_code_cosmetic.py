class DSU:
    def __init__(self, n):
        self.parent = {i: i for i in range(n)}
        self.rank = {i: 0 for i in range(n)}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union_set(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu != pv:
            if self.rank[pu] < self.rank[pv]:
                pu, pv = pv, pu
            self.parent[pv] = pu
            if self.rank[pu] == self.rank[pv]:
                self.rank[pu] += 1


class Solution:
    def countComponents(self, nums, threshold):
        limit = threshold + 1
        dsu = DSU(limit)

        for x in nums:
            mul = 2 * x
            while mul <= threshold:
                dsu.union_set(x, mul)
                mul += x

        res_set = set()
        for x in nums:
            if x <= threshold:
                res_set.add(dsu.find(x))
            else:
                res_set.add(x)

        return len(res_set)