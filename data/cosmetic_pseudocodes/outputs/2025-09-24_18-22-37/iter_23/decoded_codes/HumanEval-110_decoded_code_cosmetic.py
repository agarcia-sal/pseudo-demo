from typing import Sequence

def exchange(alpha: Sequence[int], beta: Sequence[int]) -> str:
    tally_odd: int = 0
    tally_even: int = 0

    idx_alpha: int = 0
    while idx_alpha < len(alpha):
        val = alpha[idx_alpha]
        remainder = val - 2 * (val // 2)  # val % 2 equivalently
        if remainder == 1:
            tally_odd += 1
        idx_alpha += 1

    idx_beta: int = 0
    while idx_beta < len(beta):
        val_beta = beta[idx_beta]
        rem_beta = val_beta - 2 * (val_beta // 2)  # val_beta % 2 equivalently
        if rem_beta == 0:
            tally_even += 1
        idx_beta += 1

    if tally_even >= tally_odd:
        return "YES"
    else:
        return "NO"