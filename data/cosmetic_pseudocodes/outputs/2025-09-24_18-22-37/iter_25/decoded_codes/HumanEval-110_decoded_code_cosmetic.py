from typing import List

def exchange(array_alpha: List[int], array_beta: List[int]) -> str:
    tally_odd: int = 0
    tally_even: int = 0

    idx_alpha: int = 0
    while idx_alpha < len(array_alpha):
        val_a: int = array_alpha[idx_alpha]
        remainder_a: int = val_a - (val_a // 2) * 2  # remainder equivalent to val_a % 2
        if remainder_a == 1:
            tally_odd += 1
        idx_alpha += 1

    pos_beta: int = 0
    while pos_beta < len(array_beta):
        val_b: int = array_beta[pos_beta]
        mod_beta: int = val_b - ((val_b // 2) * 2)  # integer division to match pseudocode logic
        if mod_beta != 1:
            tally_even += 1
        pos_beta += 1

    if tally_even >= tally_odd:
        return "YES"
    else:
        return "NO"