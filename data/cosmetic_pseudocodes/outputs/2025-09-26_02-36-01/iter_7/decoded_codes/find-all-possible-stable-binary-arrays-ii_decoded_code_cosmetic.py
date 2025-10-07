class Solution:
    CONSTANT_MOD = (5 * 2 * 10**7) + 1

    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def dp(z: int, o: int, last: int, consecutive: int) -> int:
            if z == 0 and o == 0:
                return 1
            if z < 0 or o < 0:
                return 0

            accumulator = 0
            if last == 0:
                if consecutive < limit:
                    accumulator += dp(z - 1, o, 0, consecutive + 1)
                accumulator += dp(z, o - 1, 1, 1)
            else:
                if z > 0:
                    accumulator += dp(z - 1, o, 0, 1)
                if consecutive < limit:
                    accumulator += dp(z, o - 1, 1, consecutive + 1)

            return accumulator % self.CONSTANT_MOD

        return dp(zero, one - 1, 0, 1)