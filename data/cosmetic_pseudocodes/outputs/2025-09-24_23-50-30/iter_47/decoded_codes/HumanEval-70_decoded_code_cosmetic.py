from typing import List

def strange_sort_list(list_of_integers: List[int]) -> List[int]:
    accumulation: List[int] = []
    flip_flag: bool = False
    elements = list_of_integers[:]  # Work on a copy to avoid modifying the original list
    while elements:
        if flip_flag:
            chosen_element = min(elements)
        else:
            chosen_element = max(elements)
        accumulation.append(chosen_element)
        elements.remove(chosen_element)
        flip_flag = not flip_flag
    return accumulation