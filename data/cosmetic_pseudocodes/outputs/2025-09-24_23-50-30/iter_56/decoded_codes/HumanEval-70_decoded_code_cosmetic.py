from typing import List

def strange_sort_list(array_of_numbers: List[int]) -> List[int]:
    accumulated_sequence: List[int] = []
    toggle: bool = False
    while array_of_numbers:
        chosen_value = max(array_of_numbers) if toggle else min(array_of_numbers)
        accumulated_sequence.append(chosen_value)
        array_of_numbers.remove(chosen_value)
        toggle = not toggle
    return accumulated_sequence