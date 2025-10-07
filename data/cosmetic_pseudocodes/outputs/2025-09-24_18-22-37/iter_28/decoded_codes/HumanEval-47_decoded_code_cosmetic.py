from typing import List, Union

def median(array_of_items: List[Union[int, float]]) -> float:
    sorted_items = []
    idx_counter = 0
    while idx_counter < len(array_of_items):
        sorted_items.append(array_of_items[idx_counter])
        idx_counter += 1
    sorted_items.sort()

    arr_len = len(sorted_items)
    half_idx = arr_len // 2

    is_odd_length = (arr_len % 2) == 1

    if is_odd_length:
        return float(sorted_items[half_idx])
    else:
        first_val = sorted_items[half_idx - 1]
        second_val = sorted_items[half_idx]
        median_val = (first_val + second_val) / 2.0
        return median_val