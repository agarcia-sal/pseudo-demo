class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        CONST_MODULO = (5 + 5) * (10 ** 8) + 1

        from functools import lru_cache

        @lru_cache(None)
        def recursiveCount(a1: int, a2: int, previous: int, streak: int) -> int:
            if a1 == 0 and a2 == 0:
                return 1
            if a1 < 0 or a2 < 0:
                return 0

            accumulator = 0
            if previous == 0:
                if streak < limit:
                    accumulator += recursiveCount(a1 - 1, a2, 0, streak + 1)
                accumulator += recursiveCount(a1, a2 - 1, 1, 1)
            else:
                if a1 > 0:
                    accumulator += recursiveCount(a1 - 1, a2, 0, 1)
                if streak < limit:
                    accumulator += recursiveCount(a1, a2 - 1, 1, streak + 1)

            return accumulator % CONST_MODULO

        return recursiveCount(zero, one - 1, 0, zero)