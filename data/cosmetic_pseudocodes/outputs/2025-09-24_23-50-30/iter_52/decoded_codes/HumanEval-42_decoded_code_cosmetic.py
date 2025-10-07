from typing import List

def incr_list(varA: List[int]) -> List[int]:
    def aux(varB: List[int], varC: int) -> List[int]:
        if varC == len(varB):
            return []
        else:
            return [varB[varC] + 1] + aux(varB, varC + 1)
    return aux(varA, 0)