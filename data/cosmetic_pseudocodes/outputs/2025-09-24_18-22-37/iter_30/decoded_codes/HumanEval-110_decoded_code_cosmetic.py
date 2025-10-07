from typing import Sequence

def exchange(alpha: Sequence[int], beta: Sequence[int]) -> str:
    tally_odd = 0
    len_one = len(alpha)
    idx_one = 0
    while idx_one < len_one:
        val_curr = alpha[idx_one]
        if val_curr % 2 == 1:
            tally_odd += 1
        idx_one += 1

    tally_even = 0
    len_two = len(beta)
    idx_two = 0
    while idx_two < len_two:
        val_curr_two = beta[idx_two]
        if val_curr_two % 2 == 0:
            tally_even += 1
        idx_two += 1

    if tally_even >= tally_odd:
        return "YES"
    else:
        return "NO"