from collections import deque
from typing import Deque, List


def is_nested(s: str) -> bool:
    open_positions: Deque[int] = deque()
    close_positions: List[int] = []

    idx = 0
    while idx < len(s):
        if s[idx] == '[':
            open_positions.append(idx)
        else:
            close_positions.append(idx)
        idx += 1

    close_length = len(close_positions)

    def process_matches(queue: Deque[int], stack: List[int], matched: int, pos: int) -> int:
        if not queue or pos >= close_length:
            return matched
        current_open = queue.popleft()
        current_close = stack[pos]
        if current_open < current_close:
            return process_matches(queue, stack, matched + 1, pos + 1)
        else:
            return process_matches(queue, stack, matched, pos)

    total_matches = process_matches(open_positions, close_positions, 0, 0)

    return total_matches >= 2