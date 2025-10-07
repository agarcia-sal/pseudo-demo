from typing import Sequence, Iterable

def total_match(array_alpha: Sequence[Iterable], array_beta: Sequence[Iterable]) -> Sequence[Iterable]:
    sum_alpha: int = 0
    sum_beta: int = 0
    iterator_a: int = 0

    while True:
        if iterator_a >= len(array_alpha):
            break
        item_a = array_alpha[iterator_a]
        length_current_a = len(item_a)
        sum_alpha += length_current_a
        iterator_a += 1

    index_b: int = 0
    while index_b < len(array_beta):
        element_b = array_beta[index_b]
        length_current_b = len(element_b)
        sum_beta += length_current_b
        index_b += 1

    if sum_alpha <= sum_beta:
        return array_alpha
    else:
        return array_beta