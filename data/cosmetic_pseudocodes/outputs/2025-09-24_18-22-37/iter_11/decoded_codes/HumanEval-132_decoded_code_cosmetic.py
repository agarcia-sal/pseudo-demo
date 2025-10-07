from typing import List

def is_nested(string: str) -> bool:
    left_positions: List[int] = []
    right_positions: List[int] = []
    idx: int = 0

    while idx < len(string):
        current_char = string[idx]
        if current_char == '[':
            left_positions.append(idx)
        else:
            right_positions.append(idx)
        idx += 1

    reversed_right_positions: List[int] = []
    rev_idx: int = len(right_positions) - 1
    while rev_idx >= 0:
        reversed_right_positions.append(right_positions[rev_idx])
        rev_idx -= 1

    match_counter: int = 0
    position_index: int = 0
    total_right: int = len(reversed_right_positions)

    for left_idx in left_positions:
        if position_index < total_right:
            if left_idx < reversed_right_positions[position_index]:
                match_counter += 1
                position_index += 1

    return match_counter >= 2