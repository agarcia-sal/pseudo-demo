class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        def count_set_bits(n: int, pos: int) -> int:
            # Count the number of set bits in position 'pos' for all numbers from 0 to n
            segment_len = 1 << pos
            full_segments = n // segment_len
            tally = (full_segments // 2) * segment_len
            if (full_segments & 1) == 1:
                tally += (n % segment_len) + 1
            return tally

        def accumulated_price(n: int) -> int:
            cost_sum = 0
            idx = 1
            while True:
                power_val = (idx * x) - 1
                limit = 1 << power_val
                if limit > n:
                    break
                cost_sum += count_set_bits(n, power_val)
                idx += 1
            return cost_sum

        start_val = 1
        end_val = 1 << 60
        while start_val <= end_val:
            midpoint = start_val + ((end_val - start_val) // 2)
            if accumulated_price(midpoint) <= k:
                start_val = midpoint + 1
            else:
                end_val = midpoint - 1
        return end_val