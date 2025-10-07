from typing import List

def strange_sort_list(sequence_of_numbers: List[int]) -> List[int]:
    output_sequence: List[int] = []
    toggle_selector: bool = False
    numbers = sequence_of_numbers[:]  # Work on a copy to avoid modifying input
    while numbers:
        if not toggle_selector:
            candidate = min(numbers)
        else:
            candidate = max(numbers)
        output_sequence.append(candidate)
        numbers.remove(candidate)
        toggle_selector = not toggle_selector
    return output_sequence