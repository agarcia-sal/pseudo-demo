from typing import List

def strange_sort_list(list_of_integers: List[int]) -> List[int]:
    result_list: List[int] = []
    pick_minimum: bool = True
    numbers = list_of_integers.copy()  # avoid modifying original list

    while numbers:
        if pick_minimum:
            chosen_value = min(numbers)
        else:
            chosen_value = max(numbers)
        result_list.append(chosen_value)
        numbers.remove(chosen_value)
        pick_minimum = not pick_minimum

    return result_list