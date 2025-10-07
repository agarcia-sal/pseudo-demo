from typing import List, Sequence, TypeVar

T = TypeVar('T', bound=Sequence)

def total_match(array_alpha: List[T], array_beta: List[T]) -> List[T]:
    sum_alpha: int = 0
    iterator_gamma: int = 1
    while iterator_gamma <= len(array_alpha):
        temp_delta: T = array_alpha[iterator_gamma - 1]
        len_epsilon: int = len(temp_delta)
        sum_alpha += len_epsilon
        iterator_gamma += 1

    sum_zeta: int = 0
    cursor_eta: int = 0
    while cursor_eta < len(array_beta):
        element_theta: T = array_beta[cursor_eta]
        length_iota: int = len(element_theta)
        sum_zeta += length_iota
        cursor_eta += 1

    if sum_alpha <= sum_zeta:
        return array_alpha
    else:
        return array_beta