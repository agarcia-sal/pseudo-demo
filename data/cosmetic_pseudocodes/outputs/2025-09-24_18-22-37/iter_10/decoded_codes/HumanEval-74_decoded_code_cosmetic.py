from typing import List, Sequence, TypeVar

T = TypeVar('T', bound=Sequence)

def total_match(list_one: List[T], list_two: List[T]) -> List[T]:
    counter_alpha: int = 0
    iterator_beta: int = 0
    accumulator_gamma: int = 0  # declared but unused as per pseudocode

    while iterator_beta < len(list_one):
        element_delta = list_one[iterator_beta]
        length_epsilon = len(element_delta)
        counter_alpha += length_epsilon
        iterator_beta += 1

    iterator_zeta: int = 0
    counter_eta: int = 0

    while True:
        if iterator_zeta >= len(list_two):
            break
        item_theta = list_two[iterator_zeta]
        size_iota = len(item_theta)
        counter_eta += size_iota
        iterator_zeta += 1

    if not (counter_alpha > counter_eta):
        return list_one
    return list_two