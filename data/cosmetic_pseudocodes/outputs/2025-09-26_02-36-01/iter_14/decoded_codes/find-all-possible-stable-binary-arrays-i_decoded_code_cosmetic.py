class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        CONSTANT_MOD = (5 * 2 * 10**7) + 1

        from functools import lru_cache

        @lru_cache(None)
        def dp(leftzeros: int, leftones: int, prevchar: int, runlen: int) -> int:
            if leftzeros == 0 and leftones == 0:
                return 1
            if leftzeros < 0 or leftones < 0:
                return 0

            acc_result = 0

            if not (prevchar == 0 and runlen >= limit):
                next_run_len = runlen + 1 if prevchar == 0 else 1
                acc_result = (acc_result + dp(leftzeros - 1, leftones, 0, next_run_len)) % CONSTANT_MOD

            if not (prevchar == 1 and runlen >= limit):
                next_run_len = runlen + 1 if prevchar == 1 else 1
                acc_result = (acc_result + dp(leftzeros, leftones - 1, 1, next_run_len)) % CONSTANT_MOD

            return acc_result

        return dp(zero, one, -1, 0)