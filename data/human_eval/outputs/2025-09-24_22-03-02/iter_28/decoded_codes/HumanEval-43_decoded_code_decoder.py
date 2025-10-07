from typing import List

def pairs_sum_to_zero(l: List[int]) -> bool:
    i = 0
    while i < len(l):
        l1 = l[i]
        j = i + 1
        while j < len(l):
            if l1 + l[j] == 0:
                return True
            j += 1
        i += 1
    return False