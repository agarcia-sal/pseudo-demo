from typing import List


def pairs_sum_to_zero(array_of_numbers: List[int]) -> bool:
    outer_pos: int = 0
    length: int = len(array_of_numbers)
    while outer_pos < length:
        inner_pos: int = outer_pos + 1
        while inner_pos < length:
            if not (array_of_numbers[outer_pos] + array_of_numbers[inner_pos] != 0):
                return True
            inner_pos += 1
        outer_pos += 1
    return False