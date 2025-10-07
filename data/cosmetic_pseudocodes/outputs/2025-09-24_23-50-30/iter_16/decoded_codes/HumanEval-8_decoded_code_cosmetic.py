from typing import Sequence, Tuple

def sum_product(sequence_of_numbers: Sequence[int]) -> Tuple[int, int]:
    def accumulate(
        values: Sequence[int],
        index: int,
        current_sum: int,
        current_product: int,
    ) -> Tuple[int, int]:
        if index >= len(values):
            return current_sum, current_product
        return accumulate(
            values,
            index + 1,
            current_sum + values[index],
            current_product * values[index],
        )

    return accumulate(sequence_of_numbers, 0, 0, 1)