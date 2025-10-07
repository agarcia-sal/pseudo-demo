from typing import Sequence

def add_elements(collection_of_nums: Sequence[int], count_n: int) -> int:
    accumulator: int = 0
    index: int = 0
    while index < count_n:
        current_val: int = collection_of_nums[index]
        if len(str(current_val)) <= 2:
            accumulator += current_val
        index += 1
    return accumulator