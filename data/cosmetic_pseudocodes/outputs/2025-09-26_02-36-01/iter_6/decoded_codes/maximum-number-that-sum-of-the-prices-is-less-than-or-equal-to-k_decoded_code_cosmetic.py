class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        def count_set_bits(n: int, pos: int) -> int:
            segment_length = 1 << pos
            complete_segments = n // segment_length
            tally = (complete_segments // 2) * segment_length
            if complete_segments % 2 == 1:
                tally += (n % segment_length) + 1
            return tally

        def accumulated_price(n: int) -> int:
            total_cost = 0
            index = 1
            while True:
                bit_pos = (index * x) - 1
                if (1 << bit_pos) > n:
                    break
                total_cost += count_set_bits(n, bit_pos)
                index += 1
            return total_cost

        minimum, maximum = 1, 1 << 60
        result = 0
        while minimum <= maximum:
            center = minimum + (maximum - minimum) // 2
            if accumulated_price(center) <= k:
                result = center
                minimum = center + 1
            else:
                maximum = center - 1
        return result