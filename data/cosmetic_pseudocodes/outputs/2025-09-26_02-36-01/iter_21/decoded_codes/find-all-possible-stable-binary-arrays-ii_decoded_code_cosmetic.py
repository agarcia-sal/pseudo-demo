class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        M = 10**9 + 1

        from functools import lru_cache

        @lru_cache(None)
        def dp(z: int, o: int, last: int, consecutive: int) -> int:
            if z < 0 or o < 0:
                return 0

            if z == 0 and o == 0:
                return one

            R = 0
            if last != zero:
                if z > 0:
                    R += dp(z - 1, o, zero, 1)
                if consecutive < limit:
                    R += dp(z, o - 1, one, consecutive + 1)
            else:
                if consecutive < limit:
                    R += dp(z - 1, o, zero, consecutive + 1)
                R += dp(z, o - 1, one, 1)

            return R % M

        return dp(zero, one - 1, zero, 0)