from typing import Sequence

def has_close_elements(sequence_of_values: Sequence[float], limit: float) -> bool:
    outer_pos = 0
    while outer_pos < len(sequence_of_values):
        first_val = sequence_of_values[outer_pos]
        inner_pos = 0
        while inner_pos < len(sequence_of_values):
            if outer_pos == inner_pos:
                inner_pos += 1
                continue
            second_val = sequence_of_values[inner_pos]
            diff_magnitude = first_val - second_val
            if diff_magnitude < 0:
                diff_magnitude = -diff_magnitude
            if diff_magnitude < limit:
                return True
            inner_pos += 1
        outer_pos += 1
    return False