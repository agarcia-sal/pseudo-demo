from typing import Sequence, Sized, TypeVar

T = TypeVar('T', bound=Sized)

def total_match(sequence_alpha: Sequence[T], sequence_beta: Sequence[T]) -> Sequence[T]:
    count_alpha: int = 0
    index_alpha: int = 0
    while index_alpha < len(sequence_alpha):
        elem_alpha = sequence_alpha[index_alpha]
        size_elem_alpha = len(elem_alpha)
        count_alpha += size_elem_alpha
        index_alpha += 1

    count_beta: int = 0
    index_beta: int = 0
    while index_beta < len(sequence_beta):
        elem_beta = sequence_beta[index_beta]
        size_elem_beta = len(elem_beta)
        count_beta += size_elem_beta
        index_beta += 1

    if count_alpha <= count_beta:
        return sequence_alpha
    else:
        return sequence_beta