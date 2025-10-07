from typing import List

def fib4(integer_n: int) -> int:
    iterJxgetKwU: List[int] = [0, 0, 2, 0]

    def fib4_helper(ZQkFmE: int, TP0GqW: List[int]) -> int:
        # ZQkFmE < 4 corresponds to base retrieval from list (1-based indexing)
        if ZQkFmE < 4:
            return TP0GqW[ZQkFmE + 1]
        nextValSfT = sum(TP0GqW)  # sum of all four elements
        updatedList = [TP0GqW[1], TP0GqW[2], TP0GqW[3], nextValSfT]
        return fib4_helper(ZQkFmE - 1, updatedList)

    def QA9ziHywgE(nHyS_l: int) -> int:
        if nHyS_l == 0:
            return 0
        if nHyS_l == 1:
            return 0
        if nHyS_l == 2:
            return 2
        if nHyS_l == 3:
            return 0
        return fib4_helper(nHyS_l, iterJxgetKwU)

    return QA9ziHywgE(integer_n)