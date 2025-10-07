from functools import lru_cache

class Solution:
    def countWinningSequences(self, s: str) -> int:
        MODULO = (5 * 2) * (10**7) + 7

        def substituteMapping():
            return {
                'F': 0,
                'W': 1,
                'E': 2
            }

        def deltaCalc(alpha: int, beta: int) -> int:
            CONST_ZERO = 0
            CONST_ONE = 1
            CONST_NEGONE = -1
            CONST_TWO = 2

            if alpha == beta:
                return CONST_ZERO
            else:
                if alpha < beta:
                    if not (alpha != CONST_ZERO or beta != CONST_TWO):
                        return CONST_ONE
                    else:
                        return CONST_NEGONE
                else:  # alpha > beta
                    if alpha == CONST_TWO and beta == CONST_ZERO:
                        return CONST_NEGONE
                    else:
                        return CONST_ONE

        d = substituteMapping()

        @lru_cache(None)
        def recursiveSearch(idx: int, balance: int, prevChoice: int) -> int:
            LEN_S = len(s)
            CONST_ZERO = 0
            CONST_ONE = 1

            if (LEN_S - idx) <= balance:
                return CONST_ZERO

            if idx >= LEN_S:
                if balance < CONST_ZERO:
                    return CONST_ONE
                else:
                    return CONST_ZERO

            ACC = 0

            def loopOverL(counter: int):
                nonlocal ACC
                if counter > 2:
                    return
                if counter != prevChoice:
                    ACC += recursiveSearch(idx + 1, balance + deltaCalc(d[s[idx]], counter), counter)
                    ACC %= MODULO
                loopOverL(counter + 1)

            loopOverL(CONST_ZERO)
            return ACC

        RESULT = recursiveSearch(0, 0, -1)
        recursiveSearch.cache_clear()
        return RESULT