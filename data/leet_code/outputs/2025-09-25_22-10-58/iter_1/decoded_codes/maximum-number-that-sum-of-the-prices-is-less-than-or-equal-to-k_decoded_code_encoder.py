class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        def count_set_bits(n: int, pos: int) -> int:
            count = 0
            block_size = 1 << pos
            full_blocks = n // block_size
            count += (full_blocks // 2) * block_size
            if full_blocks % 2 == 1:
                count += n % block_size + 1
            return count

        def accumulated_price(n: int) -> int:
            price = 0
            i = 1
            while (1 << (i * x - 1)) <= n:
                price += count_set_bits(n, i * x - 1)
                i += 1
            return price

        low, high = 1, 1 << 60
        while low <= high:
            mid = (low + high) // 2
            if accumulated_price(mid) <= k:
                low = mid + 1
            else:
                high = mid - 1
        return high