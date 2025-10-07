from collections import deque
from typing import Deque, List

def is_nested(string: str) -> bool:
    open_positions: Deque[int] = deque()
    close_positions: List[int] = []

    for i in range(len(string)):
        if string[i] == '[':
            open_positions.append(i)
        else:
            close_positions.append(i)

    matched = 0
    close_index = 0
    total_closes = len(close_positions)

    for open_index in open_positions:
        if close_index < total_closes and open_index < close_positions[close_index]:
            matched += 1
            close_index += 1

    return matched >= 2