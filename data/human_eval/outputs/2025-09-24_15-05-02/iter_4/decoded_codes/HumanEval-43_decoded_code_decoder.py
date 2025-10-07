from typing import List

def pairs_sum_to_zero(l: List[int]) -> bool:
    for i in range(len(l)):
        first_num = l[i]
        for j in range(i + 1, len(l)):
            if first_num + l[j] == 0:
                return True
    return False