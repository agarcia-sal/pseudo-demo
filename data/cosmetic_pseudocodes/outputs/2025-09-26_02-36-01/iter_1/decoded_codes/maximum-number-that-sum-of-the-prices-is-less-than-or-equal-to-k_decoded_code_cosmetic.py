class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        def bit_count(n: int, position: int) -> int:
            segment = 1 << position
            complete_segments = n // segment
            total_bits = (complete_segments // 2) * segment
            if complete_segments % 2 == 1:
                total_bits += (n % segment) + 1
            return total_bits

        def total_price(n: int) -> int:
            sum_price = 0
            index = 1
            while (1 << (index * x - 1)) <= n:
                sum_price += bit_count(n, index * x - 1)
                index += 1
            return sum_price

        start, end_ = 1, 1 << 60
        while start <= end_:
            middle = (start + end_) >> 1
            if total_price(middle) <= k:
                start = middle + 1
            else:
                end_ = middle - 1
        return end_