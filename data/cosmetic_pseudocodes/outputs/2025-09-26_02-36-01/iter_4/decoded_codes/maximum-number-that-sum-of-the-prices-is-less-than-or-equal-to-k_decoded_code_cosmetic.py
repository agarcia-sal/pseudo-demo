class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        def count_set_bits(n: int, pos: int) -> int:
            segment_length = 1 << pos
            completed_segments = n // segment_length
            half_segments = completed_segments // 2
            total = half_segments * segment_length
            if completed_segments % 2 != 0:
                remainder_length = n % segment_length
                total += remainder_length + 1
            return total

        def accumulated_price(n: int) -> int:
            cost = 0
            counter = 1
            while (1 << (counter * x - 1)) <= n:
                bit_position = counter * x - 1
                cost += count_set_bits(n, bit_position)
                counter += 1
            return cost

        left_bound, right_bound = 1, 1 << 60
        while left_bound <= right_bound:
            midpoint = left_bound + (right_bound - left_bound) // 2
            if accumulated_price(midpoint) <= k:
                left_bound = midpoint + 1
            else:
                right_bound = midpoint - 1
        return right_bound