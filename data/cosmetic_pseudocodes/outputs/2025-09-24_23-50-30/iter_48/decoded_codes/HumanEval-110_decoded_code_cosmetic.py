from typing import List

def exchange(array_alpha: List[int], array_beta: List[int]) -> str:
    count_1: int = 0
    count_2: int = 0
    index_m: int = 0
    while index_m < len(array_alpha):
        if (array_alpha[index_m] % 2) != 0:
            count_1 += 1
        index_m += 1

    index_n: int = 0
    while index_n < len(array_beta):
        if not ((array_beta[index_n] % 2) != 0):
            count_2 += 1
        index_n += 1

    if not (count_2 < count_1):
        return "YES"
    else:
        return "NO"