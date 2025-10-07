from typing import List, Sequence, TypeVar

T = TypeVar('T', bound=Sequence)

def total_match(array_alpha: List[T], array_beta: List[T]) -> List[T]:
    sum_alpha: int = 0
    counter_gamma: int = 0
    while counter_gamma < len(array_alpha):
        current_item: T = array_alpha[counter_gamma]
        size_delta: int = len(current_item)
        sum_alpha += size_delta
        counter_gamma += 1

    sum_beta: int = 0
    index_phi: int = 0
    while index_phi < len(array_beta):
        element_sigma: T = array_beta[index_phi]
        measure_tau: int = len(element_sigma)
        sum_beta += measure_tau
        index_phi += 1

    if sum_alpha <= sum_beta:
        return array_alpha
    else:
        return array_beta