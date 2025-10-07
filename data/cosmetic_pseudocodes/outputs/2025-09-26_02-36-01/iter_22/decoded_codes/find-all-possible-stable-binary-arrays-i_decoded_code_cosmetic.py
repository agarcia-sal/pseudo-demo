class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MODULO_VALUE = 10**9 + 1

        from functools import lru_cache

        @lru_cache(None)
        def dp(xyz1: int, xyz2: int, xyz3: int, xyz4: int) -> int:
            # xyz1: zeros left, xyz2: ones left
            # xyz3: last appended element (0 or 1), or -1 if none yet
            # xyz4: current consecutive count of last appended element
            if xyz1 == 0 and xyz2 == 0:
                return 1
            if xyz1 < 0 or xyz2 < 0:
                return 0

            acc_res = 0

            # Try to place '0' next if possible
            if xyz3 != 0 or xyz4 < limit:
                acc_res += dp(xyz1 - 1, xyz2, 0, xyz4 + 1 if xyz3 == 0 else 1)
                acc_res %= MODULO_VALUE

            # Try to place '1' next if possible
            if xyz3 != 1 or xyz4 < limit:
                acc_res += dp(xyz1, xyz2 - 1, 1, xyz4 + 1 if xyz3 == 1 else 1)
                acc_res %= MODULO_VALUE

            return acc_res

        return dp(zero, one, -1, 0)