from typing import Optional, Sequence

def next_smallest(seq_of_numbers: Sequence[int]) -> Optional[int]:
    processed_sequence = sorted(set(seq_of_numbers))
    if len(processed_sequence) < 2:
        return None
    return processed_sequence[1]