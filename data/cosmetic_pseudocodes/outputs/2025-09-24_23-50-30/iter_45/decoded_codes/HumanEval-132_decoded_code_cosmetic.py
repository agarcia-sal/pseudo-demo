from typing import List


def is_nested(string: str) -> bool:
    open_indices: List[int] = []
    close_indices: List[int] = []
    cursor: int = 0

    while cursor < len(string):
        if string[cursor] == '[':
            open_indices.append(cursor)
        else:
            close_indices.append(cursor)
        cursor += 1

    close_indices.reverse()
    matched_count: int = 0
    close_pos: int = 0
    max_close: int = len(close_indices)

    for open_pos in open_indices:
        if close_pos < max_close and open_pos < close_indices[close_pos]:
            matched_count += 1
            close_pos += 1

    return matched_count >= 2