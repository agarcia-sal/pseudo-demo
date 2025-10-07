from typing import List

def exchange(array_alpha: List[int], array_beta: List[int]) -> str:
    tally_odd: int = 0
    tally_even: int = 0
    pointer_a: int = 0
    while pointer_a < len(array_alpha):
        val_x: int = array_alpha[pointer_a]
        remainder_x: int = val_x - 2 * (val_x // 2)
        if remainder_x == 1:
            tally_odd += 1
        pointer_a += 1

    pointer_b: int = 0
    while pointer_b < len(array_beta):
        val_y: int = array_beta[pointer_b]
        remainder_y: int = val_y - 2 * (val_y // 2)
        if remainder_y == 0:
            tally_even += 1
        pointer_b += 1

    result_flag: int = 0
    if tally_even >= tally_odd:
        result_flag = 1

    if result_flag == 1:
        return "YES"
    else:
        return "NO"