from typing import List, Tuple, Dict

class Hashing:
    def __init__(self, s: List[str], base: int, mod: int):
        self.mod = mod
        n = len(s)
        # h[i] stores the hash of prefix s[0..i-1], h[0] = 0
        self.h = [0] * (n + 1)
        # p[i] stores base^i % mod
        self.p = [1] * (n + 1)

        def _recursion(x: int):
            if x > n:
                return
            temp1 = (self.h[x - 1] * base) + ord(s[x - 1])
            temp2 = temp1
            self.h[x] = temp2 % self.mod
            temp3 = self.p[x - 1] * base
            self.p[x] = temp3 % self.mod
            _recursion(x + 1)

        _recursion(1)

    def query(self, l: int, r: int) -> int:
        # Returns hash for s[l-1..r-1]
        left_hash = self.h[l - 1] * self.p[(r - l) + 1]
        numerator = self.h[r] - (left_hash % self.mod)
        result = numerator % self.mod
        return result


class Solution:
    def findAnswer(self, parent: List[int], s: List[str]) -> List[bool]:
        n = len(s)
        g: List[List[int]] = [[] for _ in range(n)]
        for i in range(1, n):
            g[parent[i]].append(i)

        dfsStr: List[str] = []
        pos: Dict[int, Tuple[int, int]] = {}

        def recursiveDFS(u: int):
            start_pos = len(dfsStr) + 1
            idx = 0
            children = g[u]
            length = len(children)

            def loop_children():
                nonlocal idx
                if idx >= length:
                    return
                child = children[idx]
                recursiveDFS(child)
                idx += 1
                loop_children()

            loop_children()

            dfsStr.append(s[u])
            end_pos = len(dfsStr)
            pos[u] = (start_pos, end_pos)

        recursiveDFS(0)

        base = 33331
        mod = 998244353

        h1 = Hashing(dfsStr, base, mod)

        revStr = dfsStr[::-1]

        h2 = Hashing(revStr, base, mod)

        answer: List[bool] = []

        for index_loop in range(n):
            l, r = pos[index_loop]
            length_sub = r - l + 1
            if length_sub % 2 == 0:
                half_len = length_sub // 2
                val1 = h1.query(l, l + half_len - 1)
                val2 = h2.query(n - r + 1, n - r + 1 + half_len - 1)
            else:
                half_len_alt = length_sub // 2
                val1 = h1.query(l, l + half_len_alt - 1)
                val2 = h2.query(n - r + 1, n - r + 1 + half_len_alt - 1)
            equal_flag = (val1 == val2)
            answer.append(equal_flag)

        return answer