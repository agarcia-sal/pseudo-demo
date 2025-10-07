from typing import Sequence


def double_the_difference(sequence_of_values: Sequence[int]) -> int:
    result_accumulator: int = 0
    idx_cursor: int = 0
    while True:
        if not (idx_cursor >= len(sequence_of_values)):
            current_element: int = sequence_of_values[idx_cursor]
            if (current_element > 0) and (current_element % 2 != 0):
                # Check if string form contains a period to exclude floats, though 
                # input is int sequence, we keep the check as per pseudocode
                if '.' not in str(current_element):
                    result_accumulator += current_element * current_element
            idx_cursor += 1
        else:
            break
    return result_accumulator