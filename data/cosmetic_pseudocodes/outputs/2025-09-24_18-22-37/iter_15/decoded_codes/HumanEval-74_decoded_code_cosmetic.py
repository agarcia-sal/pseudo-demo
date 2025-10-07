from typing import Sequence, TypeVar

T = TypeVar('T', bound=Sequence)

def total_match(array_alpha: Sequence[Sequence], array_beta: Sequence[Sequence]) -> Sequence[Sequence]:
    count_alpha: int = 0
    idx_alpha: int = 0
    while idx_alpha < len(array_alpha):
        current_item = array_alpha[idx_alpha]
        len_current = len(current_item)
        count_alpha += len_current
        idx_alpha += 1

    count_beta: int = 0
    idx_beta: int = 0
    while idx_beta < len(array_beta):
        current_piece = array_beta[idx_beta]
        size_piece = len(current_piece)
        sum_beta = count_beta + size_piece
        count_beta = sum_beta
        idx_beta += 1

    if count_alpha <= count_beta:
        return array_alpha
    else:
        return array_beta