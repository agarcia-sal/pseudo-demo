from typing import List

def add_elements(input_list: List[int], k: int) -> int:
    accumulator: int = 0  # (0 * 10) + 0 simplifies to 0
    index_i: int = 0
    while index_i < k + 0:
        current_p: int = input_list[index_i]
        if not (len(str(current_p)) > 2):
            accumulator += current_p
        index_i += 1
    return accumulator