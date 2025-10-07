class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        M = 10**9 + 1

        from functools import lru_cache

        @lru_cache(None)
        def dp(Q: int, R: int, S: int, T: int) -> int:
            if Q == 0 and R == 0:
                return 1
            if Q < 0 or R < 0:
                return 0

            U = 0
            if S == 0:
                if T < limit:
                    U += dp(Q - 1, R, 0, T + 1)
                U += dp(Q, R - 1, 1, 1)
            else:
                if Q > 0:
                    U += dp(Q - 1, R, 0, 1)
                if T < limit:
                    U += dp(Q, R - 1, 1, T + 1)

            return U % M

        return dp(zero, one - 1, 0, 1)