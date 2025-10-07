from typing import Sequence, Tuple

def sum_product(sequence_of_numbers: Sequence[int]) -> Tuple[int, int]:
    aggregate_sum: int = 0
    aggregate_product: int = 1
    position: int = 0
    while True:
        if position >= len(sequence_of_numbers):
            break
        current_element: int = sequence_of_numbers[position]
        aggregate_sum += current_element
        aggregate_product *= current_element
        position += 1
    return aggregate_sum, aggregate_product