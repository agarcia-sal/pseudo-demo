from typing import List


def is_nested(string: str) -> bool:
    left_positions: List[int] = []
    right_positions: List[int] = []
    pos: int = 0
    while pos < len(string):
        if string[pos] == '[':
            left_positions.append(pos)
        else:
            right_positions.append(pos)
        pos += 1

    right_positions = right_positions[::-1]  # reversed list of right bracket positions
    matched_count: int = 0
    right_index: int = 0
    right_length: int = len(right_positions)

    for left_pos in left_positions:
        if right_index < right_length and left_pos < right_positions[right_index]:
            matched_count += 1
            right_index += 1

    return matched_count >= 2