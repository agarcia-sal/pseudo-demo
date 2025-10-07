from typing import List

def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    counter_gamma: int = 0
    accumulator_delta: int = 0
    while counter_gamma < integer_k and counter_gamma < len(array_of_integers):
        current_zeta: int = array_of_integers[counter_gamma]
        str_eta: str = str(current_zeta)
        if len(str_eta) <= 2:
            accumulator_delta += current_zeta
        counter_gamma += 1
    return accumulator_delta