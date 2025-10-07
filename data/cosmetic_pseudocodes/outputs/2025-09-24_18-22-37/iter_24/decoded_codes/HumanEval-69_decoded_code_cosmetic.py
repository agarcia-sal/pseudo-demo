from typing import List

def search(list_of_integers: List[int]) -> int:
    if not list_of_integers:
        return -1
    temp_max: int = max(list_of_integers)
    freq_tracker: List[int] = [0] * (temp_max + 1)
    outer_counter: int = 0
    while outer_counter < len(list_of_integers):
        current_val: int = list_of_integers[outer_counter]
        freq_tracker[current_val] += 1
        outer_counter += 1
    result_val: int = -1
    inner_idx: int = 1
    while inner_idx <= (len(freq_tracker) - 1):
        if freq_tracker[inner_idx] >= inner_idx:
            result_val = inner_idx
        inner_idx += 1
    return result_val