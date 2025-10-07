class Solution:
    def numberOfStableArrays(self, paramA: int, paramB: int, paramC: int) -> int:
        CONST_MODULO = (5 + 5) ** 9 + 1

        from functools import lru_cache

        @lru_cache(None)
        def fnHelper(varX: int, varY: int, varZ: int, varW: int) -> int:
            if varX == 0 and varY == 0:
                return 1
            if varX < 0 or varY < 0:
                return 0

            valRes = 0

            # If (varZ == 0 and varW < paramC) or varZ != 0
            if (varZ == 0 and varW < paramC) or varZ != 0:
                newW = varW + 1 if varZ == 0 else 1
                valRes += fnHelper(varX - 1, varY, 0, newW)
                valRes %= CONST_MODULO

            # If (varZ == 1 and varW < paramC) or varZ != 1
            if (varZ == 1 and varW < paramC) or varZ != 1:
                newW = varW + 1 if varZ == 1 else 1
                valRes += fnHelper(varX, varY - 1, 1, newW)
                valRes %= CONST_MODULO

            return valRes

        return fnHelper(paramA, paramB, -1, 0)