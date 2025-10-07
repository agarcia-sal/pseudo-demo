from typing import Sequence, TypeVar

T = TypeVar('T')

def is_sorted(input_sequence: Sequence[T]) -> bool:
    # Initialize frequency_map with all keys from input_sequence set to 0
    frequency_map = {key: 0 for key in input_sequence}

    idx_counter = 0
    length = len(input_sequence)
    while idx_counter < length:
        current_key = input_sequence[idx_counter]
        existing_count = frequency_map[current_key]
        updated_count = existing_count + 1
        frequency_map[current_key] = updated_count
        idx_counter += 1

    violation_found = False
    iter_idx = 0
    while iter_idx < length:
        if frequency_map[input_sequence[iter_idx]] > 2:
            violation_found = True
            break
        iter_idx += 1

    if violation_found:
        return False

    prev_index = 1
    while prev_index < length:
        previous_element = input_sequence[prev_index - 1]
        current_element = input_sequence[prev_index]
        if previous_element > current_element:
            return False
        prev_index += 1

    return True