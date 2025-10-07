from typing import List

def strange_sort_list(list_of_integers: List[int]) -> List[int]:
    output_sequence: List[int] = []
    toggle: bool = False
    while list_of_integers:
        if not toggle:
            chosen_element = min(list_of_integers)
        else:
            chosen_element = max(list_of_integers)
        output_sequence.append(chosen_element)
        list_of_integers.remove(chosen_element)
        toggle = not toggle
    return output_sequence