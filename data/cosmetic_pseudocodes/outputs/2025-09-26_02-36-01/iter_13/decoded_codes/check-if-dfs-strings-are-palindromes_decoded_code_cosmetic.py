class Hashing:
    def __init__(self, s, base, mod):
        self.mod = mod
        self.h = [0]
        self.p = [1]

        def compute(i):
            if i > len(s):
                return
            x = self.h[i - 1] * base
            y = ord(s[i - 1])
            z = (x + y) % mod
            self.h.append(z)
            w = (self.p[i - 1] * base) % mod
            self.p.append(w)
            compute(i + 1)

        compute(1)

    def query(self, l, r):
        left_hash = self.h[l - 1] * self.p[r - l + 1]
        diff = self.h[r] - left_hash
        result = ((diff % self.mod) + self.mod) % self.mod
        return result


class Solution:
    def findAnswer(self, parent, s):
        n = len(s)
        g = [[] for _ in range(n)]

        def build(i):
            if i == n:
                return
            u = parent[i]
            if u >= 0:
                g[u].append(i)
            build(i + 1)

        build(1)

        dfsStr = []
        pos = {}

        def dfs(i):
            start_pos = len(dfsStr) + 1
            children = g[i]

            def dfs_children(index):
                if index == len(children):
                    return
                dfs(children[index])
                dfs_children(index + 1)

            dfs_children(0)
            dfsStr.append(s[i])
            end_pos = len(dfsStr)
            pos[i] = (start_pos, end_pos)

        dfs(0)

        BASE_CONST = 33331
        MOD_CONST = 998244353
        h1 = Hashing(dfsStr, BASE_CONST, MOD_CONST)

        rev_dfsStr = []

        def reverse_dfsStr(index):
            if index < 0:
                return
            rev_dfsStr.append(dfsStr[index])
            reverse_dfsStr(index - 1)

        reverse_dfsStr(len(dfsStr) - 1)
        h2 = Hashing(rev_dfsStr, BASE_CONST, MOD_CONST)

        result = []

        def process(i):
            if i == n:
                return
            l, r = pos[i]
            length = r - l + 1
            if length % 2 == 0:
                half = length // 2
                val1 = h1.query(l, l + half - 1)
                val2 = h2.query(n - r + 1, n - r + half)
            else:
                half = length // 2
                val1 = h1.query(l, l + half - 1)
                val2 = h2.query(n - r + 1, n - r + half)
            result.append(val1 == val2)
            process(i + 1)

        process(0)
        return result