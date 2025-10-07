class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        CONST_A = 10**9 + 1

        from functools import lru_cache

        @lru_cache(None)
        def delta(alpha: int, beta: int, gamma: int, deltaVal: int) -> int:
            def modAdd(x: int, y: int) -> int:
                return ((x % CONST_A) + (y % CONST_A)) % CONST_A

            if alpha == 0 and beta == 0:
                return 1
            if alpha < 0 or beta < 0:
                return 0

            accumulator = 0
            if gamma != 0 or deltaVal < limit:
                temp1 = delta(alpha - 1, beta, 0, deltaVal + 1 if gamma == 0 else 1)
                accumulator = modAdd(accumulator, temp1)

            if gamma != 1 or deltaVal < limit:
                temp2 = delta(alpha, beta - 1, 1, deltaVal + 1 if gamma == 1 else 1)
                accumulator = modAdd(accumulator, temp2)

            return accumulator

        return delta(zero, one, -1, 0)