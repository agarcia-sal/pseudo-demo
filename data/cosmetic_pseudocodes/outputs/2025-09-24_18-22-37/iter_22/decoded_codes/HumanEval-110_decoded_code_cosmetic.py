from typing import List

def exchange(array_alpha: List[int], array_beta: List[int]) -> str:
    tally_odd: int = 0
    tally_even: int = 0
    idx1: int = 0
    while idx1 < len(array_alpha):
        current_item = array_alpha[idx1]
        if not (current_item % 2 != 1):
            tally_odd += 1
        idx1 += 1
    idx2: int = 0
    while idx2 < len(array_beta):
        candidate = array_beta[idx2]
        if candidate % 2 == 0:
            tally_even += 1
        idx2 += 1
    if not (tally_even < tally_odd):
        return "YES"
    else:
        return "NO"