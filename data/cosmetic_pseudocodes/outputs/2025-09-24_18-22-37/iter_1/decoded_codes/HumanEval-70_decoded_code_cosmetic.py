from typing import List


def strange_sort_list(list_of_integers: List[int]) -> List[int]:
    result_list: List[int] = []
    pick_min: bool = True

    while list_of_integers:
        if pick_min:
            chosen_item = min(list_of_integers)
        else:
            chosen_item = max(list_of_integers)
        result_list.append(chosen_item)
        list_of_integers.remove(chosen_item)
        pick_min = not pick_min

    return result_list