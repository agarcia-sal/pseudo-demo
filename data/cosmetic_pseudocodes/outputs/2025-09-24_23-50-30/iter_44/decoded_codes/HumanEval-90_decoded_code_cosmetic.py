from typing import List, Optional


def next_smallest(array_of_numbers: List[int]) -> Optional[int]:
    filtered_sequence: List[int] = []
    for element in array_of_numbers:
        if element not in filtered_sequence:
            filtered_sequence.append(element)
    ordered_collection = sorted(filtered_sequence)
    if len(ordered_collection) < 2:
        return None
    return ordered_collection[1]