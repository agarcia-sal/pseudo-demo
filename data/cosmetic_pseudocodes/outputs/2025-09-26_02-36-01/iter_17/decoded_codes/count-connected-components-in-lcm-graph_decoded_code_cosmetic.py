class DSU:
    def __init__(self, n):
        self.parent = {}
        self.rank = {}
        a = 0
        while a < n:
            self.parent[a] = a
            self.rank[a] = 0
            a += 1

    def find(self, x):
        while self.parent[x] != x:
            h = self.find(self.parent[x])
            self.parent[x] = h
            x = h
        return x

    def union_set(self, u, v):
        p = self.find(u)
        q = self.find(v)
        if p != q:
            if self.rank[p] < self.rank[q]:
                p, q = q, p
            self.parent[q] = p
            if self.rank[p] == self.rank[q]:
                self.rank[p] += 1


class Solution:
    def countComponents(self, nums, threshold):
        r = DSU(threshold + 1)
        i = 0
        length_nums = len(nums)
        while i < length_nums:
            w = nums[i]
            k = w * 2
            while k <= threshold:
                r.union_set(w, k)
                k += w
            i += 1

        f = set()
        for z in nums:
            if z > threshold:
                f.add(z)
            else:
                tmp = r.find(z)
                f.add(tmp)
        return len(f)