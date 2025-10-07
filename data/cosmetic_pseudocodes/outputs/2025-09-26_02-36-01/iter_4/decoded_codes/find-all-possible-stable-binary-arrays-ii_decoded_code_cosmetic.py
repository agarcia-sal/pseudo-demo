class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        moduloBase = 10**9 + 1

        from functools import lru_cache

        @lru_cache(None)
        def dp(zVal: int, oVal: int, lastDigit: int, countConsecutive: int) -> int:
            if zVal == zero and oVal == zero:
                return 1
            if zVal < 0 or oVal < 0:
                return 0

            accumulator = 0

            if lastDigit == 0:
                if countConsecutive < limit:
                    accumulator += dp(zVal - 1, oVal, 0, countConsecutive + 1)
                accumulator += dp(zVal, oVal - 1, 1, 1)
            else:
                if zVal > 0:
                    accumulator += dp(zVal - 1, oVal, 0, 1)
                if countConsecutive < limit:
                    accumulator += dp(zVal, oVal - 1, 1, countConsecutive + 1)

            return accumulator % moduloBase

        return dp(zero, one - 1, 0, 0)