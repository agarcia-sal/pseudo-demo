from typing import List


def is_nested(input_text: str) -> bool:
    left_positions: List[int] = []
    right_positions: List[int] = []

    cursor: int = 0
    while cursor < len(input_text):
        current_char: str = input_text[cursor]
        if current_char == '[':
            left_positions.append(cursor)
        else:
            right_positions.append(cursor)
        cursor += 1

    right_positions.reverse()

    match_count: int = 0
    right_idx: int = 0
    right_size: int = len(right_positions)

    for left_idx in left_positions:
        if right_idx < right_size:
            if left_idx < right_positions[right_idx]:
                match_count += 1
                right_idx += 1

    if match_count >= 2:
        return True
    return False