from typing import List

def strange_sort_list(array_of_numbers: List[int]) -> List[int]:
    output_collection: List[int] = []
    toggle_marker: bool = False
    numbers = array_of_numbers.copy()  # avoid mutating the input list
    while numbers:
        if not toggle_marker:
            value_selected = min(numbers)
        else:
            value_selected = max(numbers)
        output_collection.append(value_selected)
        numbers.remove(value_selected)
        toggle_marker = not toggle_marker
    return output_collection