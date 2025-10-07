from typing import Sequence

def prime_length(data_input: Sequence[object]) -> bool:
    size_val: int = len(data_input)
    if size_val <= 1:
        return False
    index_check: int = 2
    while index_check < size_val:
        remainder_val: int = size_val - (size_val // index_check) * index_check
        if remainder_val == 0:
            return False
        index_check += 1
    return True