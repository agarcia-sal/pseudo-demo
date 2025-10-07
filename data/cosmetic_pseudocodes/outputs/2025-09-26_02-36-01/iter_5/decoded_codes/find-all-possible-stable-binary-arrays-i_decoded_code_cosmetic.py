class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD_CONST = 10**9 + 1

        from functools import lru_cache

        @lru_cache(None)
        def dp(zs: int, os: int, pc: int, prl: int) -> int:
            if zs == 0 and os == 0:
                return 1
            if zs < 0 or os < 0:
                return 0

            sum_result = 0

            # Add zero if allowed
            if pc != 0 or prl < limit:
                new_len_zero = (prl + 1) if pc == 0 else 1
                sum_result = (sum_result + dp(zs - 1, os, 0, new_len_zero)) % MOD_CONST

            # Add one if allowed
            if pc != 1 or prl < limit:
                new_len_one = (prl + 1) if pc == 1 else 1
                sum_result = (sum_result + dp(zs, os - 1, 1, new_len_one)) % MOD_CONST

            return sum_result

        return dp(zero, one, -1, 0)