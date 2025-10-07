from typing import List, Dict, Tuple

class Hashing:
    def __init__(self, s: List[str], base: int, mod: int):
        self.mod = mod
        n = len(s)
        self.h = [0] * (n + 1)
        self.p = [1] * (n + 1)
        for x in range(1, n + 1):
            self.h[x] = (self.h[x - 1] * base + ord(s[x - 1])) % mod
            self.p[x] = (self.p[x - 1] * base) % mod

    def query(self, l: int, r: int) -> int:
        diff_val = self.h[r] - self.h[l - 1] * self.p[r - l + 1]
        diff_val %= self.mod
        return diff_val

class Solution:
    def findAnswer(self, parent: List[int], s: List[str]) -> List[bool]:
        n = len(s)
        links: List[List[int]] = [[] for _ in range(n)]
        for idx in range(1, n):
            links[parent[idx]].append(idx)

        collected: List[str] = []
        boundaries: Dict[int, Tuple[int, int]] = {}

        def traverseTree(node: int):
            start_pos = len(collected) + 1
            for child in links[node]:
                traverseTree(child)
            collected.append(s[node])
            end_pos = len(collected)
            boundaries[node] = (start_pos, end_pos)

        traverseTree(0)

        BASE_CONST = 33331
        MOD_CONST = 998244353

        fwd_hash = Hashing(collected, BASE_CONST, MOD_CONST)
        rev_hash = Hashing(collected[::-1], BASE_CONST, MOD_CONST)

        results: List[bool] = []
        for z in range(n):
            st, en = boundaries[z]
            length_sub = en - st + 1
            half_len = length_sub // 2
            if length_sub % 2 == 0:
                val1 = fwd_hash.query(st, st + half_len - 1)
                val2 = rev_hash.query(n - en + 1, n - en + half_len)
            else:
                val1 = fwd_hash.query(st, st + half_len - 1) if half_len > 0 else 0
                val2 = rev_hash.query(n - en + 1, n - en + half_len) if half_len > 0 else 0
            results.append(val1 == val2)
        return results