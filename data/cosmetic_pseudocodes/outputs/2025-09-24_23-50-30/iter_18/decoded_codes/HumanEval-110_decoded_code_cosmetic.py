from typing import List

def exchange(array_alpha: List[int], array_beta: List[int]) -> str:
    count_m: int = 0
    count_n: int = 0

    idx_one: int = 0
    while idx_one < len(array_alpha):
        val_x: int = array_alpha[idx_one]
        div_x: int = val_x // 2
        if (div_x * 2) != val_x:
            count_m += 1
        idx_one += 1

    idx_two: int = 0
    while idx_two < len(array_beta):
        val_y: int = array_beta[idx_two]
        div_y: int = val_y // 2
        if (div_y * 2) == val_y:
            count_n += 1
        idx_two += 1

    if count_n < count_m:
        return "NO"
    return "YES"