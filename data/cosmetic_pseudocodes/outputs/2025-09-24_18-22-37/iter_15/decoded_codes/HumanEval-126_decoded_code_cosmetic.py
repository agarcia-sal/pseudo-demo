from typing import Sequence, TypeVar

T = TypeVar('T')

def is_sorted(sequence_elements: Sequence[T]) -> bool:
    tracker_map: dict[T, int] = {key: 0 for key in sequence_elements}
    idx_counter: int = 0
    length: int = len(sequence_elements)
    while idx_counter < length:
        current_value = sequence_elements[idx_counter]
        temp_count = tracker_map[current_value]
        new_count = temp_count + 1
        tracker_map[current_value] = new_count
        idx_counter += 1

    temp_idx: int = 0
    while temp_idx < length:
        val_to_check = sequence_elements[temp_idx]
        freq = tracker_map[val_to_check]
        if freq > 2:
            return False
        temp_idx += 1

    pointer: int = 1
    while pointer < length:
        prev_elem = sequence_elements[pointer - 1]
        curr_elem = sequence_elements[pointer]
        if not (prev_elem <= curr_elem):
            return False
        pointer += 1

    return True