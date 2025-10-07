from collections import deque
from typing import Sequence

def is_nested(string: str) -> bool:
    start_positions: deque[int] = deque()  # queue for '[' positions
    end_positions: deque[int] = deque()    # queue for non-'[' positions

    for pointer in range(len(string)):
        if string[pointer] == '[':
            start_positions.append(pointer)
        else:
            end_positions.append(pointer)

    # Convert end_positions to stack-like structure by reversing (to emulate popping from end)
    end_positions = deque(reversed(end_positions))
    matched_pairs = 0
    runner = 0
    end_length = len(end_positions)
    end_list = list(end_positions)  # allow indexed access

    for pos in start_positions:
        if runner < end_length and pos < end_list[runner]:
            matched_pairs += 1
            runner += 1

    return matched_pairs >= 2