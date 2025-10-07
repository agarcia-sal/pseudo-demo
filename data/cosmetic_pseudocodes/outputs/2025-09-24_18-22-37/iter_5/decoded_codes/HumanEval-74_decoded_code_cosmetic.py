from typing import Sequence, List

def total_match(sequence_alpha: Sequence[str], sequence_beta: Sequence[str]) -> Sequence[str]:
    sum_alpha: int = 0
    idx_alpha: int = 0
    while idx_alpha < len(sequence_alpha):
        str_item: str = sequence_alpha[idx_alpha]
        len_item: int = len(str_item)
        sum_alpha += len_item
        idx_alpha += 1

    sum_beta: int = 0
    idx_beta: int = 0
    while idx_beta < len(sequence_beta):
        str_item_beta: str = sequence_beta[idx_beta]
        len_item_beta: int = len(str_item_beta)
        sum_beta += len_item_beta
        idx_beta += 1

    if sum_alpha <= sum_beta:
        return sequence_alpha
    else:
        return sequence_beta