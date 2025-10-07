from typing import List

def strange_sort_list(list_of_integers: List[int]) -> List[int]:
    output_container: List[int] = []
    toggle_indicator: int = 1
    while list_of_integers:
        if toggle_indicator == 1:
            selected_element = min(list_of_integers)
        else:
            selected_element = max(list_of_integers)
        output_container.append(selected_element)
        list_of_integers = [item for item in list_of_integers if item != selected_element]
        toggle_indicator = (toggle_indicator + 1) % 2
    return output_container