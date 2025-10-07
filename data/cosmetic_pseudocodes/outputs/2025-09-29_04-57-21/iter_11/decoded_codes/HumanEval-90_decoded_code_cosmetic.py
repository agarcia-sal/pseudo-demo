from typing import Sequence, Optional

def next_smallest(sequence_of_numbers: Sequence[int]) -> Optional[int]:
    filtered_sorted_sequence = sorted(set(sequence_of_numbers))
    if len(filtered_sorted_sequence) < 2:
        return None
    return filtered_sorted_sequence[1]