from typing import Sequence

def exchange(collection_alpha: Sequence[int], collection_beta: Sequence[int]) -> str:
    tally_odd: int = 0
    tally_even: int = 0

    idx_alpha: int = 0
    len_alpha: int = len(collection_alpha)

    while idx_alpha < len_alpha:
        candidate_num: int = collection_alpha[idx_alpha]
        remainder_val: int = candidate_num - ( (candidate_num // 2) * 2 )
        if remainder_val == 1:
            tally_odd += 1
        idx_alpha += 1

    idx_beta: int = 0
    len_beta: int = len(collection_beta)

    while True:
        if idx_beta >= len_beta:
            break
        candidate_num_2: int = collection_beta[idx_beta]
        division_result: int = candidate_num_2 // 2
        remainder_val_2: int = candidate_num_2 - (division_result * 2)
        if remainder_val_2 == 0:
            tally_even += 1
        idx_beta += 1

    if tally_even >= tally_odd:
        return "YES"
    else:
        return "NO"