from typing import List

def exchange(array_alpha: List[int], array_beta: List[int]) -> str:
    count_1: int = 0
    count_2: int = 0
    idx_a: int = 0

    while idx_a < len(array_alpha):
        val_x: int = array_alpha[idx_a]
        if val_x % 2 == 1:
            count_1 += 1
        idx_a += 1

    idx_b: int = 0
    while True:
        if idx_b >= len(array_beta):
            break
        val_y: int = array_beta[idx_b]
        if val_y % 2 == 0:
            count_2 += 1
        idx_b += 1

    if count_2 >= count_1:
        return "YES"
    else:
        return "NO"