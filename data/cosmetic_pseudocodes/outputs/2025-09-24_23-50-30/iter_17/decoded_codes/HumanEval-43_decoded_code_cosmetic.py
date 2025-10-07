from typing import Sequence

def pairs_sum_to_zero(collection: Sequence[int]) -> bool:
    outer_ptr: int = 0
    length: int = len(collection)
    while outer_ptr < length:
        inner_ptr: int = outer_ptr + 1
        while inner_ptr < length:
            if collection[inner_ptr] == -collection[outer_ptr]:
                return True
            inner_ptr += 1
        outer_ptr += 1
    return False