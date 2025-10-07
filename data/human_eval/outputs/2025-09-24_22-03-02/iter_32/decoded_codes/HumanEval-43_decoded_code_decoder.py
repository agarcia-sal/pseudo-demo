from typing import List

def pairs_sum_to_zero(l: List[int]) -> bool:
    length = len(l)
    for i in range(length - 1):
        l1 = l[i]
        for j in range(i + 1, length):
            sum_ = l1 + l[j]
            if sum_ == 0:
                return True
    return False