from typing import List

def strange_sort_list(sequence_of_numbers: List[int]) -> List[int]:
    output_collection: List[int] = []
    toggle_indicator: bool = True
    numbers = sequence_of_numbers[:]  # copy to avoid mutating input
    while numbers:
        if toggle_indicator:
            chosen_element = min(numbers)
        else:
            chosen_element = max(numbers)
        output_collection.append(chosen_element)
        numbers.remove(chosen_element)
        toggle_indicator = not toggle_indicator
    return output_collection