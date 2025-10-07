from typing import Sequence, Tuple

def sum_product(sequence_of_numbers: Sequence[int]) -> Tuple[int, int]:
    sum_result: int = 0
    prod_result: int = 1
    index: int = 1
    length: int = len(sequence_of_numbers)
    while index <= length:
        num: int = sequence_of_numbers[index - 1]  # 1-based indexing in pseudocode
        sum_result += num
        prod_result *= num
        index += 1
    return sum_result, prod_result