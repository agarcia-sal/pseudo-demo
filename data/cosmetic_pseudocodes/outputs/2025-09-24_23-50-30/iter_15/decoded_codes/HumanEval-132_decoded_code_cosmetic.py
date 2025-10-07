from collections import deque
from typing import Deque, List


def is_nested(input_string: str) -> bool:
    left_positions: Deque[int] = deque()
    right_positions: List[int] = []

    for cursor in range(len(input_string)):
        if input_string[cursor] == '[':
            left_positions.append(cursor)
        else:
            right_positions.append(cursor)

    matched_pairs: int = 0
    right_index: int = 0
    total_right: int = len(right_positions)

    while right_index < total_right and left_positions:
        open_idx: int = left_positions.popleft()
        close_idx: int = right_positions[right_index]
        if open_idx < close_idx:
            matched_pairs += 1
            right_index += 1

    return not (matched_pairs < 2)