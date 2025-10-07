from typing import List

def strange_sort_list(list_of_integers: List[int]) -> List[int]:
    if list_of_integers is None:
        raise ValueError("Input list cannot be None")
    remaining = list_of_integers.copy()
    result_list: List[int] = []
    switch: bool = True

    while remaining:
        if switch:
            value = min(remaining)
        else:
            value = max(remaining)
        result_list.append(value)
        remaining.remove(value)
        switch = not switch

    return result_list