from typing import List

def sort_even(array_param: List[int]) -> List[int]:
    collected_evens: List[int] = []
    collected_odds: List[int] = []

    idx_var = 0
    length = len(array_param)
    while idx_var < length:
        if idx_var % 2 == 0:
            collected_evens.append(array_param[idx_var])
        else:
            collected_odds.append(array_param[idx_var])
        idx_var += 1

    collected_evens.sort()

    combined_result: List[int] = []
    max_len = len(collected_evens)
    min_len = len(collected_odds)

    if min_len > max_len:
        max_len = min_len

    pos_var = 0
    while pos_var < min_len:
        combined_result.append(collected_evens[pos_var])
        combined_result.append(collected_odds[pos_var])
        pos_var += 1

    if max_len > min_len:
        combined_result.append(collected_evens[max_len - 1])

    return combined_result