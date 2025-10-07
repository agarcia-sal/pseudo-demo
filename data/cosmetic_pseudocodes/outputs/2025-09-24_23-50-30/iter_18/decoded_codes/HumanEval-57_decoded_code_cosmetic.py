from typing import Sequence

def monotonic(input_sequence: Sequence[int]) -> bool:
    sorted_asc = sorted(input_sequence)
    sorted_desc = sorted(input_sequence, reverse=True)
    if input_sequence != sorted_asc:
        if input_sequence != sorted_desc:
            return False
    else:
        return True
    return True