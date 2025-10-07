from typing import List


def is_nested(string: str) -> bool:
    open_positions: List[int] = []
    close_positions: List[int] = []

    for idx in range(len(string)):
        if string[idx] == '[':
            open_positions.append(idx)
        else:
            close_positions.append(idx)

    close_positions.reverse()
    matched = 0
    cursor = 0
    close_len = len(close_positions)

    for pos in open_positions:
        if cursor < close_len and pos < close_positions[cursor]:
            matched += 1
            cursor += 1

    return matched >= 2