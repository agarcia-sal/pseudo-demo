class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        PRIME_CONSTANT = 10**9 + 1

        from functools import lru_cache

        @lru_cache(None)
        def computeCount(x: int, y: int, prev: int, runLength: int) -> int:
            if x < 0 or y < 0:
                return 0
            if x == 0 and y == 0:
                return 1

            accumulator = 0
            if prev == 0:
                if runLength < limit:
                    accumulator += computeCount(x - 1, y, 0, runLength + 1)
                accumulator += computeCount(x, y - 1, 1, 1)
            else:
                if x > 0:
                    accumulator += computeCount(x - 1, y, 0, 1)
                if runLength < limit:
                    accumulator += computeCount(x, y - 1, 1, runLength + 1)

            return accumulator % PRIME_CONSTANT

        return computeCount(zero, one - 1, 0, 0)