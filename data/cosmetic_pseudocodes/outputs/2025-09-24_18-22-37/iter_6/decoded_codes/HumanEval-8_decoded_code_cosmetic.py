from typing import Sequence, Tuple


def sum_product(sequence_of_numbers: Sequence[int]) -> Tuple[int, int]:
    total_accumulator: int = 0
    product_accumulator: int = 1
    index_counter: int = 0
    sequence_length: int = len(sequence_of_numbers)
    while index_counter < sequence_length:
        current_entry: int = sequence_of_numbers[index_counter]
        total_accumulator += current_entry
        product_accumulator *= current_entry
        index_counter += 1
    return total_accumulator, product_accumulator