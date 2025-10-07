from typing import List

def strange_sort_list(sequence_of_numbers: List[int]) -> List[int]:
    output_collection: List[int] = []
    toggle_indicator: bool = False
    while sequence_of_numbers:
        toggle_indicator = not toggle_indicator
        if toggle_indicator:
            candidate_value = min(sequence_of_numbers)
        else:
            candidate_value = max(sequence_of_numbers)
        output_collection.append(candidate_value)
        sequence_of_numbers.remove(candidate_value)
    return output_collection