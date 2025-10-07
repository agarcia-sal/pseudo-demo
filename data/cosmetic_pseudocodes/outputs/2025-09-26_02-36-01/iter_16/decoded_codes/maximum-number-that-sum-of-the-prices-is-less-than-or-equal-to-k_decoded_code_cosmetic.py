class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        def count_set_bits(y: int, w: int) -> int:
            # Counts total set bits in y at bit positions defined by w
            q = 0
            r = 1 << w
            s = y // r
            q += (s // 2) * r
            if s % 2 == 1:
                q += (y % r) + 1
            return q

        def accumulated_price(z: int) -> int:
            u = 0
            v = 1
            while True:
                pos = v * x - 1
                if (1 << pos) > z:
                    break
                u += count_set_bits(z, pos)
                v += 1
            return u

        a = 1
        b = 1 << 60
        while a <= b:
            c = a + (b - a) // 2
            if accumulated_price(c) <= k:
                a = c + 1
            else:
                b = c - 1
        return b