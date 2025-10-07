from typing import List

def pairs_sum_to_zero(l: List[int]) -> bool:
    length = len(l)
    for i in range(length):
        l1 = l[i]
        for j in range(i + 1, length):
            if l1 + l[j] == 0:
                return True
    return False