from typing import List

def strange_sort_list(list_of_integers: List[int]) -> List[int]:
    result_list: List[int] = []
    switch: bool = True
    remaining_values = list_of_integers[:]  # copy to avoid mutating input

    while remaining_values:
        if switch:
            chosen = min(remaining_values)
        else:
            chosen = max(remaining_values)
        result_list.append(chosen)
        remaining_values.remove(chosen)
        switch = not switch

    return result_list