class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        def count_set_bits(p: int, q: int) -> int:
            v = 1 << q
            r = p // v
            s = (r // 2) * v
            if r % 2 == 1:
                s += (p % v) + 1
            return s

        def accumulated_price(w: int) -> int:
            t = 0

            def loop_j(j: int):
                nonlocal t
                pos = j * x - 1
                if (1 << pos) <= w:
                    t += count_set_bits(w, pos)
                    loop_j(j + 1)

            loop_j(1)
            return t

        def binary_search(c: int, d: int) -> int:
            if c > d:
                return d
            e = c + (d - c) // 2
            if accumulated_price(e) <= k:
                return binary_search(e + 1, d)
            else:
                return binary_search(c, e - 1)

        return binary_search(1, 1 << 60)