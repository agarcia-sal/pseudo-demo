from typing import Sequence, Tuple


def sum_product(input_collection: Sequence[int]) -> Tuple[int, int]:
    accumulator_sum: int = 0
    accumulator_product: int = 1

    def iterate(index: int) -> None:
        nonlocal accumulator_sum, accumulator_product
        if index >= len(input_collection):
            return
        current_element = input_collection[index]
        accumulator_sum += current_element
        accumulator_product *= current_element
        iterate(index + 1)

    iterate(0)
    return accumulator_sum, accumulator_product