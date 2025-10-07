from typing import List, Optional, Tuple


def find_closest_elements(parameter_alpha: List[int]) -> Optional[Tuple[int, int]]:
    variable_gamma: Optional[Tuple[int, int]] = None
    variable_beta: Optional[int] = None
    iterator_i: int = 0

    while iterator_i < len(parameter_alpha):
        iterator_j: int = 0

        while iterator_j < len(parameter_alpha):
            condition_one: bool = iterator_i != iterator_j

            if condition_one:
                temp_diff: int = parameter_alpha[iterator_i] - parameter_alpha[iterator_j]
                temp_abs: int = -temp_diff if temp_diff < 0 else temp_diff  # absolute value without abs()

                if variable_beta is None:
                    variable_beta = temp_abs
                    temp_pair = (parameter_alpha[iterator_i], parameter_alpha[iterator_j])
                    variable_gamma = temp_pair if temp_pair[0] <= temp_pair[1] else (temp_pair[1], temp_pair[0])
                else:
                    if temp_abs < variable_beta:
                        variable_beta = temp_abs
                        temp_pair_alt = (parameter_alpha[iterator_i], parameter_alpha[iterator_j])
                        variable_gamma = temp_pair_alt if temp_pair_alt[0] <= temp_pair_alt[1] else (temp_pair_alt[1], temp_pair_alt[0])

            iterator_j += 1
        iterator_i += 1

    return variable_gamma