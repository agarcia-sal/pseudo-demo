class Solution:
    def numberOfStableArrays(self, aCount: int, bCount: int, maxRun: int) -> int:
        modulus = (5 * 2) * (10 ** 8) + 1

        from functools import lru_cache

        @lru_cache(None)
        def dp(remZero: int, remOne: int, lastDigit: int, runLength: int) -> int:
            if remZero == 0 and remOne == 0:
                return 1
            if remZero < 0 or remOne < 0:
                return 0

            resultHolder = 0
            if lastDigit == 0:
                if runLength < maxRun:
                    resultHolder += dp(remZero - 1, remOne, 0, runLength + 1)
                resultHolder += dp(remZero, remOne - 1, 1, 1)
            else:
                if remZero > 0:
                    resultHolder += dp(remZero - 1, remOne, 0, 1)
                if runLength < maxRun:
                    resultHolder += dp(remZero, remOne - 1, 1, runLength + 1)

            resultHolder %= modulus
            return resultHolder

        initialZeroCount = aCount
        initialOneCount = bCount - 1
        initialLastDigit = 0
        initialRunLength = 0
        finalAnswer = dp(initialZeroCount, initialOneCount, initialLastDigit, initialRunLength)
        return finalAnswer