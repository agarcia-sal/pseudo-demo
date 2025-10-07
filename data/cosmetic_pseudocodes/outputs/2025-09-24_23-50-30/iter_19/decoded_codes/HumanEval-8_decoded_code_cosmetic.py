from typing import Sequence, Tuple

def sum_product(sequence: Sequence[int]) -> Tuple[int, int]:
    sum_accumulator: int = 0
    prod_accumulator: int = 1
    index: int = 0
    while index < len(sequence):
        sum_accumulator += sequence[index]
        prod_accumulator *= sequence[index]
        index += 1
    return sum_accumulator, prod_accumulator