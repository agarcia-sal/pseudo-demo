from typing import Sequence

def smallest_change(input_sequence: Sequence[object]) -> int:
    counter: int = 0
    half_size: int = len(input_sequence) // 2
    cursor: int = 0

    while cursor < half_size:
        left_element = input_sequence[cursor]
        right_index = len(input_sequence) - cursor - 1
        right_element = input_sequence[right_index]

        if left_element != right_element:
            counter += 1

        cursor += 1

    return counter