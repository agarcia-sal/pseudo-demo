from typing import List

def strange_sort_list(list_of_integers: List[int]) -> List[int]:
    result_list: List[int] = []
    toggle_switch: bool = True
    while list_of_integers:
        value = min(list_of_integers) if toggle_switch else max(list_of_integers)
        result_list.append(value)
        list_of_integers.remove(value)
        toggle_switch = not toggle_switch
    return result_list