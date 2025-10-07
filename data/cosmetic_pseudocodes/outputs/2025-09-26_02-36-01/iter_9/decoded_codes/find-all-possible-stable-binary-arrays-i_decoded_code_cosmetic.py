class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MODULO_VALUE = 10**9 + 1
        from functools import lru_cache

        @lru_cache(None)
        def dp(zt_Rem: int, on_Rem: int, lastChar: int, lastLen: int) -> int:
            if zt_Rem == 0 and on_Rem == 0:
                return 1
            if zt_Rem < 0 or on_Rem < 0:
                return 0

            accRes = 0

            if not (lastChar == 0 and lastLen >= limit):
                nextRunLen = lastLen + 1 if lastChar == 0 else 1
                accRes = (accRes + dp(zt_Rem - 1, on_Rem, 0, nextRunLen)) % MODULO_VALUE

            if not (lastChar == 1 and lastLen >= limit):
                nextRunLen = lastLen + 1 if lastChar == 1 else 1
                accRes = (accRes + dp(zt_Rem, on_Rem - 1, 1, nextRunLen)) % MODULO_VALUE

            return accRes

        return dp(zero, one, -1, 0)