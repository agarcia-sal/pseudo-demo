class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        def count_set_bits(n: int, pos: int) -> int:
            segment_size = 1 << pos  # 2 ** pos
            complete_segments = n // segment_size
            accumulator = (complete_segments // 2) * segment_size
            if complete_segments % 2 == 1:
                accumulator += (n % segment_size) + 1
            return accumulator

        def accumulated_price(n: int) -> int:
            total = 0
            index = 1
            while True:
                power_val = (index * x) - 1
                if (1 << power_val) > n:
                    break
                total += count_set_bits(n, power_val)
                index += 1
            return total

        start, end_val = 1, 1 << 60
        result = 0
        while start <= end_val:
            midpoint = (start + end_val) // 2
            if accumulated_price(midpoint) <= k:
                result = midpoint
                start = midpoint + 1
            else:
                end_val = midpoint - 1
        return result