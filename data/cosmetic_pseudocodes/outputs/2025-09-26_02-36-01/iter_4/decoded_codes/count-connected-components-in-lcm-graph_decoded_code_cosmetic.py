class DSU:
    def __init__(self, n):
        self.parent = {i: i for i in range(n)}
        self.rank = {i: 0 for i in range(n)}

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
            x = self.parent[x]
        return self.parent[x]

    def union_set(self, u, v):
        u = self.find(u)
        v = self.find(v)
        if u != v:
            if not (self.rank[u] >= self.rank[v]):
                u, v = v, u
            self.parent[v] = u
            if self.rank[u] == self.rank[v]:
                self.rank[u] += 1


class Solution:
    def countComponents(self, nums, threshold):
        dsu = DSU(threshold + 1)
        idx1 = 0
        while idx1 < len(nums):
            num = nums[idx1]
            multiplier = 2
            product = num * multiplier
            while product <= threshold:
                dsu.union_set(num, product)
                multiplier += 1
                product = num * multiplier
            idx1 += 1

        unique_parents = set()
        idx2 = 0
        while idx2 < len(nums):
            number = nums[idx2]
            if number <= threshold:
                parent_rep = dsu.find(number)
                unique_parents.add(parent_rep)
            else:
                unique_parents.add(number)
            idx2 += 1

        return len(unique_parents)