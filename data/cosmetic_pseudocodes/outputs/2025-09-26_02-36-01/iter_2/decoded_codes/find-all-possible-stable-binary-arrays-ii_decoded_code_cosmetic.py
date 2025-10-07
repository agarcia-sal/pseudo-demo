class Solution:
    def numberOfStableArrays(self, countZero: int, countOne: int, maxConsecutive: int) -> int:
        MODULUS = 1_000_000_001

        from functools import lru_cache

        @lru_cache(None)
        def dp(zerosLeft: int, onesLeft: int, previous: int, streakLength: int) -> int:
            if zerosLeft == 0 and onesLeft == 0:
                return 1
            if zerosLeft < 0 or onesLeft < 0:
                return 0

            accumulator = 0
            if previous == 0:
                if streakLength < maxConsecutive:
                    accumulator += dp(zerosLeft - 1, onesLeft, 0, streakLength + 1)
                accumulator += dp(zerosLeft, onesLeft - 1, 1, 1)
            else:
                if zerosLeft > 0:
                    accumulator += dp(zerosLeft - 1, onesLeft, 0, 1)
                if streakLength < maxConsecutive:
                    accumulator += dp(zerosLeft, onesLeft - 1, 1, streakLength + 1)

            return accumulator % MODULUS

        return dp(countZero, countOne - 1, 0, 1)