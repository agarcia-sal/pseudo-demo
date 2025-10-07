class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MODULO_CONST = 10**9 + 1

        from functools import lru_cache

        @lru_cache(None)
        def recursiveHelper(remainingZeroes: int, remainingOnes: int, previousChar: int, previousRun: int) -> int:
            if remainingZeroes == 0 and remainingOnes == 0:
                return 1
            if remainingZeroes < 0 or remainingOnes < 0:
                return 0

            def addModulo(a: int, b: int) -> int:
                return (a + b) % MODULO_CONST

            answerHolder = 0

            if (previousChar != 0) or (previousRun < limit):
                nextRunLength = previousRun + 1 if previousChar == 0 else 1
                answerHolder = addModulo(answerHolder, recursiveHelper(remainingZeroes - 1, remainingOnes, 0, nextRunLength))

            if (previousChar != 1) or (previousRun < limit):
                nextCount = previousRun + 1 if previousChar == 1 else 1
                answerHolder = addModulo(answerHolder, recursiveHelper(remainingZeroes, remainingOnes - 1, 1, nextCount))

            return answerHolder

        return recursiveHelper(zero, one, -1, 0)