from typing import Sequence

def pairs_sum_to_zero(numbers_collection: Sequence[int]) -> bool:
    outer_pos = 0
    length = len(numbers_collection)
    while outer_pos < length - 1:
        current_num = numbers_collection[outer_pos]
        inner_pos = outer_pos + 1
        while inner_pos < length:
            if current_num + numbers_collection[inner_pos] == 0:
                return True
            inner_pos += 1
        outer_pos += 1
    return False