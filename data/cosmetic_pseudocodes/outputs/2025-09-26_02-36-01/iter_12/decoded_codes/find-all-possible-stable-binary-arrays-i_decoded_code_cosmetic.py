class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        BASE_MODULUS = 10**9 + 1

        from functools import lru_cache

        @lru_cache(None)
        def recurse(remainingZeros: int, remainingOnes: int, prevChar: int, runLen: int) -> int:
            def moduloSum(a: int, b: int) -> int:
                total = a + b
                if total >= BASE_MODULUS:
                    total -= BASE_MODULUS
                return total

            if remainingZeros == 0 and remainingOnes == 0:
                return 1
            if remainingZeros < 0 or remainingOnes < 0:
                return 0

            accumulator = 0

            if not (prevChar == 0 and runLen >= limit):
                newRunLen = runLen + 1 if prevChar == 0 else 1
                partialResult = recurse(remainingZeros - 1, remainingOnes, 0, newRunLen)
                accumulator = moduloSum(accumulator, partialResult)

            if not (prevChar == 1 and runLen >= limit):
                updatedRunLen = runLen + 1 if prevChar == 1 else 1
                partialRes2 = recurse(remainingZeros, remainingOnes - 1, 1, updatedRunLen)
                accumulator = moduloSum(accumulator, partialRes2)

            return accumulator

        startPrevChar = -1
        startRunLength = 0

        return recurse(zero, one, startPrevChar, startRunLength)