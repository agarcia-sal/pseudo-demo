from typing import List


def strange_sort_list(array_of_numbers: List[int]) -> List[int]:
    output_array: List[int] = []
    toggle_indicator: bool = False
    numbers = array_of_numbers[:]  # Copy to avoid modifying input list
    while len(numbers) > 0:
        toggle_indicator = not toggle_indicator
        if toggle_indicator:
            chosen_element = min(numbers)
        else:
            chosen_element = max(numbers)
        output_array.append(chosen_element)
        numbers.remove(chosen_element)
    return output_array