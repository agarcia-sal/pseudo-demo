class DSU:
    def __init__(self, n):
        self.parent = {}
        self.rank = {}
        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 0

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union_set(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u == root_v:
            return
        if self.rank[root_u] < self.rank[root_v]:
            root_u, root_v = root_v, root_u
        self.parent[root_v] = root_u
        if self.rank[root_u] == self.rank[root_v]:
            self.rank[root_u] += 1


class Solution:
    def countComponents(self, nums, threshold):
        dsu = DSU(threshold + 1)

        for number in nums:
            multiple = number * 2
            while multiple <= threshold:
                dsu.union_set(number, multiple)
                multiple += number

        representatives = set()
        for number in nums:
            if number <= threshold:
                representatives.add(dsu.find(number))
            else:
                representatives.add(number)

        return len(representatives)