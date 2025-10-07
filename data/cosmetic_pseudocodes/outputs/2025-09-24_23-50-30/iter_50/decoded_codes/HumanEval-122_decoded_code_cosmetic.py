from typing import List

def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    accumulate_total: int = 0
    index_pointer: int = 0  # defined as in pseudocode, though unused explicitly after init

    def process_element(position: int) -> None:
        nonlocal accumulate_total
        if position >= integer_k:
            return
        current_val = array_of_integers[position]
        str_len = len(str(current_val))
        if str_len <= 2:
            accumulate_total += current_val
        process_element(position + 1)

    process_element(0)
    return accumulate_total