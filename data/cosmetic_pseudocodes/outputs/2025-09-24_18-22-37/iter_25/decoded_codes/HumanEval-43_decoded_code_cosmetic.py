from typing import List

def pairs_sum_to_zero(list_of_integers: List[int]) -> bool:
    p = 0
    n = len(list_of_integers)
    while p < n - 1:
        q = p + 1
        while q < n:
            sum_temp = list_of_integers[p] + list_of_integers[q]
            if sum_temp == 0:
                return True
            q += 1
        p += 1
    return False