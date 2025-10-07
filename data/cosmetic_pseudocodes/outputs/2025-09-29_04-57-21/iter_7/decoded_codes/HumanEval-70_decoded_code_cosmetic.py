from typing import List

def strange_sort_list(sequence_of_numbers: List[int]) -> List[int]:
    output_collection: List[int] = []
    toggle: bool = False
    sequence = sequence_of_numbers[:]  # make a copy to avoid mutating input
    while sequence:
        if not toggle:
            chosen_element = min(sequence)
        else:
            chosen_element = max(sequence)
        output_collection.append(chosen_element)
        sequence.remove(chosen_element)
        toggle = not toggle
    return output_collection