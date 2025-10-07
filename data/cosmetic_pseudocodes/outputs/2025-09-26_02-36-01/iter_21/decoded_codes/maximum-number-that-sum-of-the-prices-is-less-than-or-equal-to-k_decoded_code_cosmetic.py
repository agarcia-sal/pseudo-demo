class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        def count_set_bits(a: int, b: int) -> int:
            y = 1 << b  # 2 ** b
            w = a // y
            z = (w // 2) * y
            if (w % 2) == 1:
                z += (a % y) + 1
            return z

        def accumulated_price(m: int) -> int:
            def alt_loop(c: int, d: int, e: int) -> int:
                if e > m:
                    return c
                f = count_set_bits(m, d)
                return alt_loop(c + f, d + x, d + x)
            return alt_loop(0, x, x)

        r, s = 1, 1 << 60  # s = 2^60

        def binary_search(t: int, u: int) -> int:
            if t > u:
                return u
            mid_val = (t + u) // 2
            if accumulated_price(mid_val) <= k:
                return binary_search(mid_val + 1, u)
            else:
                return binary_search(t, mid_val - 1)

        return binary_search(r, s)