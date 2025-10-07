class Hashing:
    def __init__(self, s, base, mod):
        self.mod = mod
        self.h = [0] * (len(s) + 1)
        self.p = [1] * (len(s) + 1)
        for index in range(1, len(s) + 1):
            val = (self.h[index - 1] * base + ord(s[index - 1])) % mod
            self.h[index] = val
            power = (self.p[index - 1] * base) % mod
            self.p[index] = power

    def query(self, l, r):
        diff = (self.h[r] - self.h[l - 1] * self.p[r - l + 1]) % self.mod
        if diff < 0:
            diff += self.mod
        return diff


class Solution:
    def findAnswer(self, parent, s):
        n = len(s)
        adjacency_list = [[] for _ in range(n)]
        for idx in range(1, n):
            adjacency_list[parent[idx]].append(idx)

        dfsStr = []
        pos = {}

        def dfs(node):
            start_pos = len(dfsStr) + 1  # 1-based indexing
            for child in adjacency_list[node]:
                dfs(child)
            dfsStr.append(s[node])
            end_pos = len(dfsStr)
            pos[node] = (start_pos, end_pos)

        dfs(0)

        base_val = 33331
        mod_val = 998244353

        h1 = Hashing(dfsStr, base_val, mod_val)
        reversed_dfsStr = dfsStr[::-1]
        h2 = Hashing(reversed_dfsStr, base_val, mod_val)

        result = []
        for i in range(n):
            left, right = pos[i]
            length = right - left + 1
            if length % 2 == 0:
                half_len = length // 2
                val1 = h1.query(left, left + half_len - 1)
                val2 = h2.query(n - right + 1, n - right + half_len)
            else:
                half_len = (length + 1) // 2
                val1 = h1.query(left, left + half_len - 1)
                val2 = h2.query(n - right + 1, n - right + half_len)
            result.append(val1 == val2)
        return result