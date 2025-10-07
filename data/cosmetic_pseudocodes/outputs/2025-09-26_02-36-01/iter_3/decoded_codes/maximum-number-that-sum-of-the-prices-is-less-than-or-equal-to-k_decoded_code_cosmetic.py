class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        def count_set_bits(n: int, pos: int) -> int:
            segment_len = 1 << pos
            completed_cycles = n // segment_len
            tally = (completed_cycles // 2) * segment_len
            if (completed_cycles % 2) != 0:
                remainder = (n % segment_len) + 1
                tally += remainder
            return tally

        def accumulated_price(n: int) -> int:
            total_cost = 0
            index = 1
            while True:
                exponent = (index * x) - 1
                power_val = 1 << exponent
                if power_val > n:
                    break
                total_cost += count_set_bits(n, exponent)
                index += 1
            return total_cost

        left, right = 1, 1 << 60
        while left <= right:
            middle = left + (right - left) // 2
            if accumulated_price(middle) <= k:
                left = middle + 1
            else:
                right = middle - 1
        return right