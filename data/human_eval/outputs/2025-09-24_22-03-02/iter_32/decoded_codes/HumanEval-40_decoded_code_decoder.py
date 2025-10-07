from typing import List

def triples_sum_to_zero(l: List[int]) -> bool:
    n = len(l)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                s = l[i] + l[j] + l[k]
                if s == 0:
                    return True
    return False