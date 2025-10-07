from typing import Sequence


def pairs_sum_to_zero(collection_of_numbers: Sequence[int]) -> bool:
    outer_index: int = 0
    length = len(collection_of_numbers)
    while outer_index < length:
        first_value = collection_of_numbers[outer_index]
        inner_index = outer_index + 1
        while inner_index < length:
            second_value = collection_of_numbers[inner_index]
            if first_value + second_value == 0:
                return True
            inner_index += 1
        outer_index += 1
    return False