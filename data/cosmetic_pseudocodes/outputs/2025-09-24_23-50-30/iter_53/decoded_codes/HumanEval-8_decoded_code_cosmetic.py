from typing import Sequence, Tuple

def sum_product(number_sequence: Sequence[int]) -> Tuple[int, int]:
    def iterate(accumulator_sum: int, accumulator_product: int, remaining_sequence: Sequence[int]) -> Tuple[int, int]:
        if not remaining_sequence:
            return accumulator_sum, accumulator_product
        head_element = remaining_sequence[0]
        tail_sequence = remaining_sequence[1:]
        return iterate(accumulator_sum + head_element, accumulator_product * head_element, tail_sequence)
    return iterate(0, 1, number_sequence)