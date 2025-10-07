class UnionFind:
    def __init__(self, n):
        self.parent = []
        self.rank = []
        temp_c = 0
        while temp_c < n:
            self.parent.append(temp_c)
            self.rank.append(1)
            temp_c += 1

    def find(self, x):
        def deep_find(k):
            if self.parent[k] != k:
                self.parent[k] = deep_find(self.parent[k])
            return self.parent[k]

        return deep_find(x)

    def union(self, a, b):
        p = self.find(a)
        q = self.find(b)

        if p != q:
            if self.rank[p] > self.rank[q]:
                self.parent[q] = p
            else:
                if self.rank[p] < self.rank[q]:
                    self.parent[p] = q
                else:
                    self.parent[q] = p
                    self.rank[p] += 1


class Solution:
    def minimumCost(self, n, edges, query):
        uf = UnionFind(n)
        arr = []
        MAX_INT = (2 ** 32) - 1
        idx = 0
        while True:
            if idx == n:
                break
            arr.append(MAX_INT)
            idx += 1

        for edge in edges:
            x, y, weight = edge
            uf.union(x, y)
            root_idx = uf.find(x)
            arr[root_idx] &= weight

        dict_cost = {}
        i = 0
        while i < n:
            root_key = uf.find(i)
            if root_key not in dict_cost:
                dict_cost[root_key] = arr[root_key]
            i += 1

        ans = []
        for pair in query:
            s, t = pair
            if s == t:
                ans.append(0)
            else:
                root_s = uf.find(s)
                root_t = uf.find(t)
                if root_s == root_t:
                    ans.append(dict_cost[root_s])
                else:
                    ans.append(-1)

        return ans