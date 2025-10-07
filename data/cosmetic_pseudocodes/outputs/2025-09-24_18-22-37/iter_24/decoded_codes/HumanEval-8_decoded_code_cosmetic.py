from typing import List, Tuple

def sum_product(array_of_numbers: List[int]) -> Tuple[int, int]:
    accumulator_alpha: int = 0
    accumulator_beta: int = 1
    iterator_rho: int = 0
    length_tau: int = len(array_of_numbers)
    while iterator_rho < length_tau:
        current_delta: int = array_of_numbers[iterator_rho]
        increment_epsilon: int = accumulator_alpha + current_delta
        multiplier_zeta: int = accumulator_beta * current_delta
        accumulator_alpha = increment_epsilon
        accumulator_beta = multiplier_zeta
        iterator_rho += 1
    return accumulator_alpha, accumulator_beta