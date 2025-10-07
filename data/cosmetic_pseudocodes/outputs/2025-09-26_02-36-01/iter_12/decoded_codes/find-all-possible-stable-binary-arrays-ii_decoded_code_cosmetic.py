class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        CONSTRAINT = 10**9 + 1

        from functools import lru_cache

        @lru_cache(None)
        def recur(a: int, b: int, prev: int, streak: int) -> int:
            if a == 0 and b == 0:
                return one
            if a < 0 or b < 0:
                return zero

            accumulator = 0
            if prev == zero:
                if streak < limit:
                    accumulator += recur(a - 1, b, zero, streak + 1)
                accumulator += recur(a, b - 1, one, 1)
            else:  # prev == one or prev == -1 initially
                if a > 0:
                    accumulator += recur(a - 1, b, zero, 1)
                if streak < limit:
                    accumulator += recur(a, b - 1, one, streak + 1)

            return accumulator % CONSTRAINT

        return recur(zero, one, -1, 0)