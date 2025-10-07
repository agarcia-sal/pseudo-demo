from typing import List

def strange_sort_list(list_of_integers: List[int]) -> List[int]:
    result_list: List[int] = []
    selection_flag: bool = True
    while list_of_integers:
        if selection_flag:
            val = min(list_of_integers)
        else:
            val = max(list_of_integers)
        result_list.append(val)
        list_of_integers.remove(val)
        selection_flag = not selection_flag
    return result_list