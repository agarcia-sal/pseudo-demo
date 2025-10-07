from typing import List

def strange_sort_list(list_of_integers: List[int]) -> List[int]:
    result_list: List[int] = []
    selection_switch = True
    while list_of_integers:
        if selection_switch:
            val = min(list_of_integers)
        else:
            val = max(list_of_integers)
        result_list.append(val)
        list_of_integers.remove(val)
        selection_switch = not selection_switch
    return result_list