from typing import List

def strange_sort_list(list_of_integers: List[int]) -> List[int]:
    result_list = []
    toggle = True
    while list_of_integers:
        if toggle:
            value = min(list_of_integers)
        else:
            value = max(list_of_integers)
        result_list.append(value)
        list_of_integers.remove(value)
        toggle = not toggle
    return result_list