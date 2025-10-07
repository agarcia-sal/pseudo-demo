from typing import List

def pairs_sum_to_zero(l0: List[int]) -> bool:
    indexA: int = 0
    indexB: int = 1
    n: int = len(l0)
    while indexA < n - 1:
        while True:
            if indexB > n - 1:
                indexA += 1
                indexB = indexA + 2
            else:
                if (l0[indexA] + l0[indexB]) == 0:
                    return True
                indexB += 1
            if indexB > n - 1 or (indexB > 0 and (l0[indexA] + l0[indexB - 1]) == 0):
                break
    return False