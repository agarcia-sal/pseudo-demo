from typing import List

def is_nested(string: str) -> bool:
    left_positions: List[int] = []
    right_positions: List[int] = []
    current_pos: int = 0
    length: int = len(string)
    while current_pos < length:
        if string[current_pos] == "[":
            left_positions.append(current_pos)
        else:
            right_positions.append(current_pos)
        current_pos += 1
    right_positions.reverse()
    matched: int = 0
    right_index: int = 0
    total_right: int = len(right_positions)
    for left_index in left_positions:
        if not (right_index >= total_right or left_index >= right_positions[right_index]):
            matched += 1
            right_index += 1
    return matched >= 2