class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        def count_set_bits(n: int, pos: int) -> int:
            b = 1 << pos
            f = n // b
            s = (f // 2) * b
            if f % 2 == 1:
                s += (n % b) + 1
            return s

        def accumulated_price(n: int) -> int:
            total = 0
            idx = 1
            while True:
                exp_term = idx * x - 1
                pow_val = 1 << exp_term
                if pow_val > n:
                    break
                total += count_set_bits(n, exp_term)
                idx += 1
            return total

        low_val, hi_val = 1, 1 << 60

        while low_val <= hi_val:
            median = low_val + (hi_val - low_val) // 2
            if accumulated_price(median) <= k:
                low_val = median + 1
            else:
                hi_val = median - 1
        return hi_val