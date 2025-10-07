from typing import Sequence, Tuple

def sum_product(sequence_of_nums: Sequence[int]) -> Tuple[int, int]:
    total_sum: int = 0
    total_prod: int = 1
    position: int = 0

    while position < len(sequence_of_nums):
        current_element: int = sequence_of_nums[position]
        interim_sum: int = total_sum + current_element
        interim_prod: int = total_prod * current_element

        total_sum = interim_sum
        total_prod = interim_prod

        position += 1

    return total_sum, total_prod