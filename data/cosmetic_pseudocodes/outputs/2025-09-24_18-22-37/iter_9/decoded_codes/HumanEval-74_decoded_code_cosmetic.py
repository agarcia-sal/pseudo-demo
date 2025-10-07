from typing import Sequence, Optional, List, TypeVar

T = TypeVar('T', bound=Sequence)

def total_match(vals_alpha: Sequence[T], vals_beta: Sequence[T]) -> Sequence[T]:
    accum_alpha: int = 0
    curr_item_alpha: Optional[T] = None
    curr_index_alpha: int = 0
    while curr_index_alpha < len(vals_alpha):
        curr_item_alpha = vals_alpha[curr_index_alpha]
        partial_len_alpha = len(curr_item_alpha)
        accum_alpha += partial_len_alpha
        curr_index_alpha += 1

    accum_beta: int = 0
    curr_item_beta: Optional[T] = None
    curr_index_beta: int = 0
    while curr_index_beta != len(vals_beta):
        curr_item_beta = vals_beta[curr_index_beta]
        part_len_beta = len(curr_item_beta)
        accum_beta += part_len_beta
        curr_index_beta += 1

    result_list: Optional[Sequence[T]] = None
    if accum_alpha <= accum_beta:
        result_list = vals_alpha
    else:
        result_list = vals_beta

    return result_list