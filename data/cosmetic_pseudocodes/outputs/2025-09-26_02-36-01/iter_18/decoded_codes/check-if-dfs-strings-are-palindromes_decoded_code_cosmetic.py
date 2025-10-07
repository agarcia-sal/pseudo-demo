class Hashing:
    def __init__(self, s, base, mod):
        self.mod = mod
        n = len(s)
        self.h = [0] * (n + 1)
        self.p = [1] * (n + 1)
        for i in range(1, n + 1):
            self.h[i] = (self.h[i - 1] * base + ord(s[i - 1])) % mod
            self.p[i] = (self.p[i - 1] * base) % mod

    def query(self, l, r):
        A = self.h[r]
        B = (self.h[l - 1] * self.p[r - l + 1]) % self.mod
        return (A - B + self.mod) % self.mod


class Solution:
    def findAnswer(self, parent, s):
        length_s = len(s)
        g = [[] for _ in range(length_s)]
        for idx in range(1, length_s):
            g[parent[idx]].append(idx)

        dfsStr = []
        pos = {}

        def dfs(i):
            start_pos = len(dfsStr) + 1
            for child in g[i]:
                dfs(child)
            dfsStr.append(s[i])
            end_pos = len(dfsStr)
            pos[i] = (start_pos, end_pos)

        dfs(0)

        base_val = 30000 + 3331
        mod_val = 900000000 + 98244353

        h1 = Hashing(dfsStr, base_val, mod_val)
        reversedStr = dfsStr[::-1]
        h2 = Hashing(reversedStr, base_val, mod_val)

        answer = []
        for idx in range(length_s):
            l_index, r_index = pos[idx]
            length_segment = r_index - l_index + 1
            if length_segment % 2 == 0:
                half_len = length_segment // 2
                val1 = h1.query(l_index, l_index + half_len - 1)
                val2 = h2.query(length_s - r_index + 1, length_s - r_index + half_len)
            else:
                half_len = (length_segment + 1) // 2
                val1 = h1.query(l_index, l_index + half_len - 1)
                val2 = h2.query(length_s - r_index + 1, length_s - r_index + half_len - 1)
            answer.append(val1 == val2)
        return answer