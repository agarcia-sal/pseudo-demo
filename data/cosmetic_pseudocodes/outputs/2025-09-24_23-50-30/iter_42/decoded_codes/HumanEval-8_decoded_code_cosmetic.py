from typing import Sequence, Tuple

def sum_product(sequence_of_numbers: Sequence[int | float]) -> Tuple[int | float, int | float]:
    support_count: int = 0
    accumulator_product: int | float = 1
    accumulator_sum: int | float = 0
    while support_count < len(sequence_of_numbers):
        accumulator_sum += sequence_of_numbers[support_count]
        accumulator_product *= sequence_of_numbers[support_count]
        support_count += 1
    return accumulator_sum, accumulator_product