from typing import List


def is_nested(string: str) -> bool:
    left_positions: List[int] = []
    right_positions: List[int] = []
    cursor: int = 0

    while cursor < len(string):
        symbol = string[cursor]
        if symbol == '[':
            left_positions.append(cursor)
        else:
            right_positions.append(cursor)
        cursor += 1

    reversed_right_positions: List[int] = []
    idx_right: int = len(right_positions) - 1
    while idx_right >= 0:
        reversed_right_positions.append(right_positions[idx_right])
        idx_right -= 1

    valid_pairs: int = 0
    idx_right_cursor: int = 0
    total_right: int = len(reversed_right_positions)

    for pos_left in left_positions:
        if idx_right_cursor < total_right and pos_left < reversed_right_positions[idx_right_cursor]:
            valid_pairs += 1
            idx_right_cursor += 1

    return not (valid_pairs < 2)