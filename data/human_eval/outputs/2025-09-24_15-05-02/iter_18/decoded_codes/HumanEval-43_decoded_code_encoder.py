from typing import List

def pairs_sum_to_zero(l: List[int]) -> bool:
    for i, l1 in enumerate(l):
        for j in range(i + 1, len(l)):
            if l1 + l[j] == 0:
                return True
    return False