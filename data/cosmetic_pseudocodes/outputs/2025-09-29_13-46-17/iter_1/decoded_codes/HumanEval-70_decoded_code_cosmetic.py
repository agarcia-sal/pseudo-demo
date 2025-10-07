from typing import List

def strange_sort_list(list_of_integers: List[int]) -> List[int]:
    result_list: List[int] = []
    select_min: bool = True

    while list_of_integers:
        if select_min:
            chosen_value = min(list_of_integers)
        else:
            chosen_value = max(list_of_integers)
        result_list.append(chosen_value)
        list_of_integers.remove(chosen_value)
        select_min = not select_min

    return result_list