class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        def count_set_bits(n: int, pos: int) -> int:
            seg = 1 << pos
            full = n // seg
            ret = (full // 2) * seg
            if full % 2 == 1:
                ret += (n % seg) + 1
            return ret

        def accumulated_price(n: int) -> int:
            total = 0
            idx = 1
            while (1 << ((idx * x) - 1)) <= n:
                total += count_set_bits(n, (idx * x) - 1)
                idx += 1
            return total

        lo, hi = 1, 1 << 60
        while lo <= hi:
            mid = (lo + hi) // 2
            if accumulated_price(mid) <= k:
                lo = mid + 1
            else:
                hi = mid - 1
        return hi