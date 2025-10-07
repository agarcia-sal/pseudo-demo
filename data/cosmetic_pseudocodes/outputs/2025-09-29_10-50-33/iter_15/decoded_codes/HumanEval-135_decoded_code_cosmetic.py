from typing import Sequence

def can_arrange(data_sequence: Sequence[int]) -> int:
    position_marker: int = -1
    current_step: int = 1

    while current_step < len(data_sequence):
        if not data_sequence[current_step - 1] <= data_sequence[current_step]:
            position_marker = current_step
        current_step += 1

    return position_marker