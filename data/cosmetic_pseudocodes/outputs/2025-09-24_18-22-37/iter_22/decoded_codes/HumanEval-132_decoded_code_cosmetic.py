from typing import List


def is_nested(text: str) -> bool:
    left_positions: List[int] = []
    right_positions: List[int] = []
    iterator: int = 0
    length = len(text)
    while iterator <= length - 1:
        current_ch = text[iterator]
        if current_ch == '[':
            left_positions.append(iterator)
        else:
            right_positions.append(iterator)
        iterator += 1

    idx: int = 0
    len_right: int = len(right_positions)
    total: int = 0
    reversed_right: List[int] = right_positions[::-1]

    while idx < len(left_positions):
        left_idx = left_positions[idx]
        if idx < len_right:
            if left_idx < reversed_right[idx]:
                total += 1
        idx += 1

    return total >= 2