from typing import List

def strange_sort_list(list_of_integers: List[int]) -> List[int]:
    output_sequence: List[int] = []
    toggle_indicator: bool = False
    integers = list_of_integers.copy()  # Avoid modifying input list
    while integers:
        if not toggle_indicator:
            selected_element = min(integers)
        else:
            selected_element = max(integers)
        output_sequence.append(selected_element)
        integers.remove(selected_element)
        toggle_indicator = not toggle_indicator
    return output_sequence