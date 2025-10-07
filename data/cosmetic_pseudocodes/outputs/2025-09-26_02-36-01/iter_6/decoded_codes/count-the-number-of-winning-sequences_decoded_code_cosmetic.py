class Solution:
    def countWinningSequences(self, strInput: str) -> int:
        CONST_MOD = 1_000_000_007
        d = {"F": 0, "W": 1, "E": 2}

        def compute(valA: int, valB: int) -> int:
            if valA == valB:
                return 0
            elif (valA - valB) ** 2 == (valB - valA) ** 2 and valA < valB:
                if valA == 0 and valB == 2:
                    return 1
                else:
                    return -1
            elif valA == 2 and valB == 0:
                return -1
            else:
                return 1

        # Cache to avoid recomputation: key = (idxX, remY, prevZ)
        from functools import lru_cache

        @lru_cache(None)
        def explore(idxX: int, remY: int, prevZ: int) -> int:
            remaining_len = len(strInput) - idxX
            if remaining_len <= remY:
                return 0
            if idxX >= len(strInput):
                if remY < 0:
                    return 1
                else:
                    return 0

            finalResult = 0

            def helperMod(value: int, modNum: int) -> int:
                while value >= modNum:
                    value -= modNum
                return value

            for currL in [0, 1, 2]:
                if currL != prevZ:
                    tempSum = explore(idxX + 1, remY + compute(d[strInput[idxX]], currL), currL)
                    finalResult += tempSum
                    finalResult = helperMod(finalResult, CONST_MOD)

            return finalResult

        answer = explore(0, 0, -1)
        # CLEAR_CACHE equivalent (no action needed since lru_cache clears on function exit)

        return answer