class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        M = 10**9 + 1

        from functools import lru_cache

        @lru_cache(None)
        def innerDp(x: int, y: int, previous: int, chain: int) -> int:
            if x == 0 and y == 0:
                return 1
            if x < 0 or y < 0:
                return 0

            total = 0
            if previous == 0:
                if chain < limit:
                    total += innerDp(x - 1, y, 0, chain + 1)
                total += innerDp(x, y - 1, 1, 1)
            else:
                if x > 0:
                    total += innerDp(x - 1, y, 0, 1)
                if chain < limit:
                    total += innerDp(x, y - 1, 1, chain + 1)

            return total % M

        # last is set to -1 to indicate no previous element; zero is 0
        return innerDp(zero, one, -1, zero)