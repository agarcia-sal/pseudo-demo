from typing import List

def sort_even(original_sequence: List[int]) -> List[int]:
    evens_temp: List[int] = []
    odds_temp: List[int] = []
    idx: int = 0

    while idx < len(original_sequence):
        evens_temp.append(original_sequence[idx])
        idx += 2

    idx = 1
    while idx < len(original_sequence):
        odds_temp.append(original_sequence[idx])
        idx += 2

    evens_temp.sort()
    merged_output: List[int] = []
    evens_count: int = len(evens_temp)
    odds_count: int = len(odds_temp)
    idx = 0

    while idx < min(evens_count, odds_count):
        pair_item = (evens_temp[idx], odds_temp[idx])
        merged_output.append(pair_item[0])
        merged_output.append(pair_item[1])
        idx += 1

    if evens_count > odds_count:
        merged_output.append(evens_temp[evens_count - 1])

    return merged_output