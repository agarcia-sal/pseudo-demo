class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        CONST_MOD = 10**9 + 1

        from functools import lru_cache

        @lru_cache(None)
        def dp(qwe: int, rty: int, uio: int, pas: int) -> int:
            if qwe == 0 and rty == 0:
                return 1
            if qwe < 0 or rty < 0:
                return 0

            cnt = 0

            if uio != 0 or pas < limit:
                cnt += dp(qwe - 1, rty, 0, pas + 1 if uio == 0 else 1)
                cnt = (cnt % CONST_MOD + CONST_MOD) % CONST_MOD  # handle modulo properly

            if uio != 1 or pas < limit:
                cnt += dp(qwe, rty - 1, 1, pas + 1 if uio == 1 else 1)
                cnt %= CONST_MOD

            return cnt

        return dp(zero, one, -1, 0)