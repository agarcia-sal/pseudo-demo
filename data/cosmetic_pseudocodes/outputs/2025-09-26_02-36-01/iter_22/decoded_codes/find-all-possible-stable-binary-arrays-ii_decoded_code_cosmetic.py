class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        modBase = 10**9 + 1

        from functools import lru_cache

        @lru_cache(None)
        def dp(z: int, o: int, last: int, consecutive: int) -> int:
            # Base cases
            if z == 0 and o == 0:
                return 1
            if z < 0 or o < 0:
                return 0

            acc = 0
            if last == 0:
                # Last chosen element is zero
                if consecutive < limit:
                    acc += dp(z - 1, o, 0, consecutive + 1)
                acc += dp(z, o - 1, 1, 1)
            else:
                # Last chosen element is one
                if z > 0:
                    acc += dp(z - 1, o, 0, 1)
                if consecutive < limit:
                    acc += dp(z, o - 1, 1, consecutive + 1)

            return acc % modBase

        return dp(zero, one - 1, 0, 1)