from typing import Sequence

def exchange(array_alpha: Sequence[int], array_beta: Sequence[int]) -> str:
    tally_a: int = 0
    tally_b: int = 0
    idx_x: int = 0
    while idx_x < len(array_alpha):
        val_x: int = array_alpha[idx_x]
        if val_x % 2 != 0:
            tally_a += 1
        idx_x += 1
    idx_y: int = 0
    while idx_y < len(array_beta):
        val_y: int = array_beta[idx_y]
        if val_y % 2 == 0:
            tally_b += 1
        idx_y += 1
    if not (tally_b < tally_a):
        return "YES"
    return "NO"