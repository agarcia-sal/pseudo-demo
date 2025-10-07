from typing import List

def strange_sort_list(arr_elements: List[int]) -> List[int]:
    outcome_collection: List[int] = []
    toggle_indicator: bool = True
    while arr_elements:
        chosen_value = min(arr_elements) if toggle_indicator else max(arr_elements)
        outcome_collection.append(chosen_value)
        for idx in range(len(arr_elements)):
            if arr_elements[idx] == chosen_value:
                arr_elements.pop(idx)
                break
        toggle_indicator = not toggle_indicator
    return outcome_collection