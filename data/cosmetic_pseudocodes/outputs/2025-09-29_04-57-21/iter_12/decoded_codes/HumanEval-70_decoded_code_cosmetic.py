from typing import List

def strange_sort_list(list_of_integers: List[int]) -> List[int]:
    output_sequence: List[int] = []
    toggle_indicator: bool = False
    elements = list_of_integers[:]  # Copy to avoid modifying the input list
    while elements:
        if not toggle_indicator:
            chosen_element = min(elements)
        else:
            chosen_element = max(elements)
        output_sequence.append(chosen_element)
        elements.remove(chosen_element)  # remove first occurrence of chosen element
        toggle_indicator = not toggle_indicator
    return output_sequence