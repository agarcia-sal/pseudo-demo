from typing import List

def strange_sort_list(list_of_integers: List[int]) -> List[int]:
    result: List[int] = []
    switch: bool = True
    remaining_values = list_of_integers.copy()
    while remaining_values:
        if switch:
            chosen_value = min(remaining_values)
        else:
            chosen_value = max(remaining_values)
        result.append(chosen_value)
        remaining_values.remove(chosen_value)
        switch = not switch
    return result