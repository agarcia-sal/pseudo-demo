class DSU:
    def __init__(self, n):
        self.parent = {}
        self.rank = {}
        index = 0
        while index < n:
            self.parent[index] = index
            self.rank[index] = 0
            index += 1

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]  # Path compression
            x = self.parent[x]
        return x

    def union_set(self, u, v):
        u = self.find(u)
        v = self.find(v)
        if u != v:
            if self.rank[u] < self.rank[v]:
                u, v = v, u
            self.parent[v] = u
            if self.rank[u] == self.rank[v]:
                self.rank[u] += 1


class Solution:
    def countComponents(self, nums, threshold):
        dsu = DSU(threshold + 1)
        idx_outer = 0
        while idx_outer < len(nums):
            val = nums[idx_outer]
            idx_inner = val * 2
            while idx_inner <= threshold:
                dsu.union_set(val, idx_inner)
                idx_inner += val
            idx_outer += 1

        unique_parents = set()
        for el in nums:
            if el <= threshold:
                unique_parents.add(dsu.find(el))
            else:
                unique_parents.add(el)
        return len(unique_parents)