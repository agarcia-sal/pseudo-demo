class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        modBase = (5 * 2 * 10**8) + 1  # 5 * 2 * 10^8 + 1 = 1000000001

        from functools import lru_cache

        @lru_cache(None)
        def dp(remainingZeros: int, remainingOnes: int, prevChar: int, prevCount: int) -> int:
            if remainingZeros == 0 and remainingOnes == 0:
                return 1
            if remainingZeros < 0 or remainingOnes < 0:
                return 0

            accumulator = 0

            if prevChar != 0 or prevCount < limit:
                nextRunLength = prevCount + 1 if prevChar == 0 else 1
                recurseResult = dp(remainingZeros - 1, remainingOnes, 0, nextRunLength)
                accumulator += recurseResult
                # Equivalent to: accumulator -= (accumulator // modBase) * modBase
                # Use modulo operation directly instead:
                accumulator %= modBase

            if prevChar != 1 or prevCount < limit:
                subsequentRunLength = prevCount + 1 if prevChar == 1 else 1
                nextResult = dp(remainingZeros, remainingOnes - 1, 1, subsequentRunLength)
                accumulator += nextResult
                accumulator %= modBase

            return accumulator

        return dp(zero, one, -1, 0)