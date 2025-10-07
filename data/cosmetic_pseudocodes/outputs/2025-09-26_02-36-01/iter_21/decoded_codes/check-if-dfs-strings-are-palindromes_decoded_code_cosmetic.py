from typing import List, Tuple, Dict


class Hashing:
    def __init__(self, s: List[str], base: int, mod: int):
        self.mod = mod
        n = len(s)
        self.h = [0] * (n + 1)  # prefix hashes
        self.p = [1] * (n + 1)  # powers of base mod mod

        def loop_var(x: int, y: int) -> None:
            if x > y:
                return
            z = self.h[x - 1] * base + ord(s[x - 1])
            u = z % self.mod
            self.h[x] = u
            w = (self.p[x - 1] * base) % self.mod
            self.p[x] = w
            loop_var(x + 1, y)

        loop_var(1, n)

    def query(self, l: int, r: int) -> int:
        diff = self.h[r] - (self.h[l - 1] * self.p[r - l + 1]) % self.mod
        res = diff % self.mod
        return res


class Solution:
    def findAnswer(self, parent: List[int], s: str) -> List[bool]:
        n = len(s)
        g: List[List[int]] = [[] for _ in range(n)]

        def build_graph(idx: int) -> None:
            if idx >= n:
                return

            def inner_build(j: int) -> None:
                if j >= n:
                    return
                pi = parent[j]
                if idx == pi:
                    g[idx].append(j)
                inner_build(j + 1)

            inner_build(0)
            build_graph(idx + 1)

        build_graph(0)

        dfsStr: List[str] = []
        pos: Dict[int, Tuple[int, int]] = {}

        def dfs(i: int) -> None:
            l = len(dfsStr) + 1

            def visit_children(k: int) -> None:
                if k >= len(g[i]):
                    return
                child = g[i][k]
                dfs(child)
                visit_children(k + 1)

            visit_children(0)
            dfsStr.append(s[i])
            r = len(dfsStr)
            pos[i] = (l, r)

        dfs(0)

        base = 33331
        mod = 998244353
        h1 = Hashing(dfsStr, base, mod)

        revStr: List[str] = []

        def reverse_append(idx: int) -> None:
            if idx < 0:
                return
            revStr.append(dfsStr[idx])
            reverse_append(idx - 1)

        reverse_append(len(dfsStr) - 1)
        h2 = Hashing(revStr, base, mod)

        ans: List[bool] = []

        def process_index(t: int) -> None:
            if t >= n:
                return
            l, r = pos[t]
            length = r - l + 1
            mid = length // 2
            k_mod_2_is_zero = (length - 2 * mid) == 0
            # Both branches do the same query operations, safe to keep as is:
            v1 = h1.query(l, l + mid - 1) if mid > 0 else 0
            v2 = h2.query(n - r + 1, (n - r + 1) + mid - 1) if mid > 0 else 0
            ans.append(v1 == v2)
            process_index(t + 1)

        process_index(0)
        return ans