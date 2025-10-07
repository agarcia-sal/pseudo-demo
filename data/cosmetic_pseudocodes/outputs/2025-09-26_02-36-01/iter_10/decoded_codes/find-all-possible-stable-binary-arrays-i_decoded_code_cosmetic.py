class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MODCONST = 10**9 + 1

        from functools import lru_cache

        @lru_cache(None)
        def internalDP(remZeros: int, remOnes: int, prevChar: int, runLen: int) -> int:
            if remZeros == 0 and remOnes == 0:
                return 1
            if remZeros < 0 or remOnes < 0:
                return 0

            accVal = 0

            if prevChar != 0 or runLen < limit:
                nxt_runLen = runLen + 1 if prevChar == 0 else 1
                accVal = (accVal + internalDP(remZeros - 1, remOnes, 0, nxt_runLen)) % MODCONST

            if prevChar != 1 or runLen < limit:
                nxt_runLen = runLen + 1 if prevChar == 1 else 1
                accVal = (accVal + internalDP(remZeros, remOnes - 1, 1, nxt_runLen)) % MODCONST

            return accVal

        return internalDP(zero, one, -1, 0)