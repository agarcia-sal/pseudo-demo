class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        CONST_MODULUS = 10**9 + 1

        from functools import lru_cache

        @lru_cache(None)
        def dp(z: int, o: int, last: int, consecutive: int) -> int:
            if z == 0 and o == 0:
                # Both zero and one used up
                return 1
            if z < 0 or o < 0:
                return 0

            result = 0
            if last == 0:
                if consecutive < limit:
                    result += dp(z - 1, o, 0, consecutive + 1)
                result += dp(z, o - 1, 1, 1)
            else:
                if z > 0:
                    result += dp(z - 1, o, 0, 1)
                if consecutive < limit:
                    result += dp(z, o - 1, 1, consecutive + 1)

            return result % CONST_MODULUS

        # Start by choosing zero digit first with zero consecutive count
        # Note: one - 1 because we already consume one of 'one' in the initial call with last=0 and consecutive=0
        return dp(zero, one - 1, 0, 0)