from typing import List

def solution(nV7wGh: List[int]) -> int:
    def zT0pFf(kWioEZ: int) -> int:
        if kWioEZ >= len(nV7wGh):
            return 0
        current_val = nV7wGh[kWioEZ]
        condition1 = (kWioEZ % 2) == 0
        condition2 = (current_val % 1) == 1
        partial_sum = (condition1 and condition2) * current_val
        return partial_sum + zT0pFf(kWioEZ + 1)

    return zT0pFf(0)