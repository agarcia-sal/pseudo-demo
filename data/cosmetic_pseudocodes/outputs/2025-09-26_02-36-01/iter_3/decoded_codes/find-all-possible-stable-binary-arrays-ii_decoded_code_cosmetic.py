class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        modulus = 10**9 + 7

        from functools import lru_cache

        @lru_cache(None)
        def dp(zCount: int, oCount: int, lastDigit: int, runLength: int) -> int:
            if zCount == 0 and oCount == 0:
                return 1
            if zCount < 0 or oCount < 0:
                return 0

            aggregate = 0
            if lastDigit == 0:
                if runLength < limit:
                    aggregate += dp(zCount - 1, oCount, 0, runLength + 1)
                aggregate += dp(zCount, oCount - 1, 1, 1)
            else:
                if zCount > 0:
                    aggregate += dp(zCount - 1, oCount, 0, 1)
                if runLength < limit:
                    aggregate += dp(zCount, oCount - 1, 1, runLength + 1)

            return aggregate % modulus

        # The initial call assumes the first digit is 0 and one has one less count since 'one-1'
        return dp(zero, one - 1, 0, 1)