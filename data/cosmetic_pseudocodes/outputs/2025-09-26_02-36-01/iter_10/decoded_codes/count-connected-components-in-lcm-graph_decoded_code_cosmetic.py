class DSU:
    def __init__(self, n):
        self.parent = {i: i for i in range(n)}
        self.rank = {i: 0 for i in range(n)}

    def find(self, x):
        def locate(y):
            if self.parent[y] != y:
                self.parent[y] = locate(self.parent[y])
            return self.parent[y]
        return locate(x)

    def union_set(self, u, v):
        def combine(a, b):
            a = self.find(a)
            b = self.find(b)
            if a != b:
                if self.rank[a] < self.rank[b]:
                    a, b = b, a
                self.parent[b] = a
                if self.rank[a] == self.rank[b]:
                    self.rank[a] += 1
        combine(u, v)


class Solution:
    def countComponents(self, nums, threshold):
        disjointSet = DSU(threshold + 1)
        for num in nums:
            k = num * 2
            while k <= threshold:
                disjointSet.union_set(num, k)
                k += num

        parentsSet = set()
        for num in nums:
            if num <= threshold:
                parentsSet.add(disjointSet.find(num))
            else:
                parentsSet.add(num)

        return len(parentsSet)