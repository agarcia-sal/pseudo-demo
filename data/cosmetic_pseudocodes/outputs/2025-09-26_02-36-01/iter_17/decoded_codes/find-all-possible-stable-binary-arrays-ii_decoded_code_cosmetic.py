class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        M = 10**9 + 1

        from functools import lru_cache

        @lru_cache(None)
        def dp(zcount: int, ocount: int, lastVal: int, streak: int) -> int:
            if zcount == 0 and ocount == 0:
                return 1
            if zcount < 0 or ocount < 0:
                return 0

            accumulator = 0

            if lastVal == 0:
                if streak < limit:
                    accumulator += dp(zcount - 1, ocount, 0, streak + 1)
                accumulator += dp(zcount, ocount - 1, 1, 1)
            else:
                if zcount > 0:
                    accumulator += dp(zcount - 1, ocount, 0, 1)
                if streak < limit:
                    accumulator += dp(zcount, ocount - 1, 1, streak + 1)

            return accumulator % M

        return dp(zero, one - 1, 0, 0)