from typing import Sequence, TypeVar

T = TypeVar('T', bound=Sequence)

def total_match(list_one: Sequence[Sequence], list_two: Sequence[Sequence]) -> Sequence[Sequence]:
    accumulator_alpha: int = 0
    iterator_beta: int = 0

    while iterator_beta < len(list_one):
        temp_gamma = list_one[iterator_beta]
        increment_delta = len(temp_gamma)
        accumulator_alpha += increment_delta
        iterator_beta += 1

    accumulator_epsilon: int = 0
    iterator_zeta: int = 0

    while iterator_zeta < len(list_two):
        temp_eta = list_two[iterator_zeta]
        length_theta = len(temp_eta)
        accumulator_epsilon += length_theta
        iterator_zeta += 1

    condition_iota = accumulator_alpha <= accumulator_epsilon
    if condition_iota:
        return list_one
    else:
        return list_two