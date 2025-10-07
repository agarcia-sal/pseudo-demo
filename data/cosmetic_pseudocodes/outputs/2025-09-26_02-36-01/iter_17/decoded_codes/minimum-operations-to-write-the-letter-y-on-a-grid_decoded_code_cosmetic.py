from collections import defaultdict
from math import floor

class Solution:
    def minimumOperationsToWriteY(self, grid):
        p = len(grid)
        q = floor(p / 2)
        w = set()

        a = 0
        while a <= q:
            w.add((a, a))
            a += 1

        b = 0
        while b <= q:
            w.add((b, p - b - 1))
            b += 1

        c = q
        while c <= p - 1:
            w.add((c, q))
            c += 1

        d_map = defaultdict(int)
        e_map = defaultdict(int)

        for r, s in w:
            d_map[grid[r][s]] += 1

        for x in range(p):
            for y in range(p):
                if (x, y) not in w:
                    e_map[grid[x][y]] += 1

        v = float('inf')

        for y_idx in range(3):
            for n_idx in range(3):
                if y_idx != n_idx:
                    s1 = sum(d_map.values()) - d_map.get(y_idx, 0)
                    s2 = sum(e_map.values()) - e_map.get(n_idx, 0)
                    op_total = s1 + s2
                    if op_total < v:
                        v = op_total

        return v