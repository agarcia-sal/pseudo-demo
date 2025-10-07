from typing import Sequence, Tuple

def sum_product(sequence_of_numbers: Sequence[int]) -> Tuple[int, int]:
    total_accum: int = 0
    accum_factor: int = 1
    for element in sequence_of_numbers:
        total_accum += element
        accum_factor *= element
    return total_accum, accum_factor