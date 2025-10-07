from typing import List, Union

def exchange(array_alpha: List[int], array_beta: List[int]) -> str:
    tally_odd: int = 0
    tally_even: int = 0

    for current_val_alpha in array_alpha:
        if current_val_alpha % 2 == 1:
            tally_odd += 1

    for current_val_beta in array_beta:
        if current_val_beta % 2 != 1:
            tally_even += 1

    if not (tally_even < tally_odd):
        return "YES"
    else:
        return "NO"