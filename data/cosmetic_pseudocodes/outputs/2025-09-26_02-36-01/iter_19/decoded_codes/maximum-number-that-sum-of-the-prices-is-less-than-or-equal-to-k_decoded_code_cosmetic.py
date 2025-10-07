class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        def count_set_bits(n: int, pos: int) -> int:
            block_sz = 1 << pos
            whole_blocks = n // block_sz
            addend = (whole_blocks // 2) * block_sz
            tally = addend
            if (whole_blocks % 2) == 1:
                remainder = (n % block_sz) + 1
                tally += remainder
            return tally

        def accumulated_price(n: int) -> int:
            sum_price = 0
            index = 1
            while (1 << (index * x - 1)) <= n:
                factor = index * x - 1
                bits_counted = count_set_bits(n, factor)
                sum_price += bits_counted
                index += 1
            return sum_price

        start = 1
        end = 1 << 60
        while start <= end:
            middle = start + (end - start) // 2
            if accumulated_price(middle) <= k:
                start = middle + 1
            else:
                end = middle - 1
        return end