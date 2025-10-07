from typing import List


def is_nested(string: str) -> bool:
    open_indices: List[int] = []
    close_indices: List[int] = []
    idx: int = 0
    while idx < len(string):
        if string[idx] == '[':
            open_indices.append(idx)
        else:
            close_indices.append(idx)
        idx += 1

    reversed_close_indices: List[int] = []
    i: int = len(close_indices) - 1
    while i >= 0:
        reversed_close_indices.append(close_indices[i])
        i -= 1

    matched_count: int = 0
    pos_in_close: int = 0
    max_pos: int = len(reversed_close_indices)
    for opening_pos in open_indices:
        if pos_in_close < max_pos and opening_pos < reversed_close_indices[pos_in_close]:
            matched_count += 1
            pos_in_close += 1

    return matched_count >= 2