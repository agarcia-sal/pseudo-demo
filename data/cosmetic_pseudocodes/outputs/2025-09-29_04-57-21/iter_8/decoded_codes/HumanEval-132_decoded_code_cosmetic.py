from typing import List

def is_nested(string: str) -> bool:
    left_indices: List[int] = []
    right_indices: List[int] = []
    cursor: int = 0
    while cursor < len(string):
        if string[cursor] == '[':
            left_indices.append(cursor)
        else:
            right_indices.append(cursor)
        cursor += 1
    right_indices.reverse()
    tally: int = 0
    marker: int = 0
    total_right: int = len(right_indices)
    for left_pos in left_indices:
        if marker < total_right and left_pos < right_indices[marker]:
            tally += 1
            marker += 1
    return tally >= 2