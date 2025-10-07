from typing import List

def triples_sum_to_zero(list_l: List[int]) -> bool:
    n = len(list_l)
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if list_l[i] + list_l[j] + list_l[k] == 0:
                    return True
    return False