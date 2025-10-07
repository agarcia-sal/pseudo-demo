class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 1

        from functools import lru_cache

        @lru_cache(None)
        def internalCompute(remZero: int, remOne: int, prev: int, streak: int) -> int:
            if remZero == 0 and remOne == 0:
                return 1
            if remZero < 0 or remOne < 0:
                return 0

            acc = 0
            if prev == 0:
                if streak < limit:
                    acc += internalCompute(remZero - 1, remOne, 0, streak + 1)
                acc += internalCompute(remZero, remOne - 1, 1, 1)
            else:
                if remZero > 0:
                    acc += internalCompute(remZero - 1, remOne, 0, 1)
                if streak < limit:
                    acc += internalCompute(remZero, remOne - 1, 1, streak + 1)

            return acc % MOD

        return internalCompute(zero, one - 1, 0, 1)