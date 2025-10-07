from typing import List

def strange_sort_list(list_of_integers: List[int]) -> List[int]:
    output_sequence: List[int] = []
    toggle_switch: bool = False
    while list_of_integers:
        toggle_switch = not toggle_switch
        if toggle_switch:
            chosen_element = min(list_of_integers)
        else:
            chosen_element = max(list_of_integers)
        output_sequence.append(chosen_element)
        list_of_integers.remove(chosen_element)
    return output_sequence