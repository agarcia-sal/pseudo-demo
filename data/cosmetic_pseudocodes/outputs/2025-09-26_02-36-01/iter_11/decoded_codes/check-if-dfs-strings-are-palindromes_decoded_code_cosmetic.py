class Hashing:
    def __init__(self, s, base, mod):
        self.mod = mod
        n = len(s)
        self.h = [0] * (n + 1)
        self.p = [1] * (n + 1)
        for idx in range(1, n + 1):
            temp1 = (self.h[idx - 1] * base) % mod
            temp2 = ord(s[idx - 1])
            self.h[idx] = (temp1 + temp2) % mod
            self.p[idx] = (self.p[idx - 1] * base) % mod

    def query(self, l, r):
        diff = self.h[r] - (self.h[l - 1] * self.p[r - l + 1]) % self.mod
        result = diff % self.mod
        return result


class Solution:
    def findAnswer(self, parent, s):
        pos = {}
        dfsStr = []
        n = len(s)
        g = [[] for _ in range(n)]
        for i in range(1, n):
            g[parent[i]].append(i)

        def dfs(i):
            left_pos = len(dfsStr) + 1
            for child in g[i]:
                dfs(child)
            dfsStr.append(s[i])
            right_pos = len(dfsStr)
            pos[i] = (left_pos, right_pos)

        dfs(0)

        base = 33331
        mod = 998244353
        h1 = Hashing(dfsStr, base, mod)
        reversed_str = dfsStr[::-1]
        h2 = Hashing(reversed_str, base, mod)

        ans = []
        for i in range(n):
            l, r = pos[i]
            length_sub = r - l + 1
            if length_sub % 2 == 0:
                half_len = length_sub // 2
                v1 = h1.query(l, l + half_len - 1)
                start_h2 = n - r + 1
                v2 = h2.query(start_h2, start_h2 + half_len - 1)
            else:
                half_len = length_sub // 2
                v1 = h1.query(l, l + half_len - 1)
                start_h2 = n - r + 1
                v2 = h2.query(start_h2, start_h2 + half_len - 1)
            ans.append(v1 == v2)
        return ans