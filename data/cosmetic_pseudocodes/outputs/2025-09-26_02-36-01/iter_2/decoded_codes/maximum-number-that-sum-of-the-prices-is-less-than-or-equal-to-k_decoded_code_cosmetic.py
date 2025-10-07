class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        def count_set_bits(n: int, pos: int) -> int:
            segment_length = 1 << pos
            complete_segments = n // segment_length
            total = (complete_segments // 2) * segment_length
            if complete_segments % 2 != 0:
                total += (n % segment_length) + 1
            return total

        def accumulated_price(n: int) -> int:
            sum_price = 0
            index = 1
            while (1 << (index * x - 1)) <= n:
                sum_price += count_set_bits(n, index * x - 1)
                index += 1
            return sum_price

        left_bound, right_bound = 1, 1 << 60

        while left_bound <= right_bound:
            middle = left_bound + (right_bound - left_bound) // 2
            if accumulated_price(middle) <= k:
                left_bound = middle + 1
            else:
                right_bound = middle - 1

        return right_bound