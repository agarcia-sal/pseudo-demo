from typing import List


def is_nested(string: str) -> bool:
    left_positions: List[int] = []
    right_positions: List[int] = []
    cursor: int = 0
    while cursor < len(string):
        if string[cursor] == '[':
            left_positions.append(cursor)
        else:
            right_positions.append(cursor)
        cursor += 1

    right_positions = right_positions[::-1]
    total_right: int = len(right_positions)
    matched: int = 0
    offset: int = 0
    while offset < total_right:
        if offset >= len(left_positions):
            break
        if left_positions[offset] < right_positions[offset]:
            matched += 1
            offset += 1
        else:
            offset += 1
    return matched >= 2